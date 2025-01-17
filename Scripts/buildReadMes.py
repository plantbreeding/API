#! /usr/bin/env python

import yaml
import glob
import sys
import json
import dereferenceAll
import re

def buildStringExample(fieldName, strSchema):
	strExample = ''
	if('enum' in strSchema):
		strExample = strSchema['enum']
	elif('format' in strSchema):
		if 'date' == strSchema['format']:
			strExample = '2018-01-01'
		elif 'date-time' == strSchema['format']:
			strExample = '2018-01-01T14:47:23-0600'
	else:
		strExample = fieldName
		print('WARNING: generic String example generated, example missing from spec in ' + fieldName)
		
	return strExample

def buildArrayExample(fieldName, schema):
	arr = []
	
	if 'example' in schema:
		arr = schema['example']
	elif 'items' in schema:
		itemSchema = schema['items']
		if ('type' in itemSchema):
			if (itemSchema['type'] == 'string'):
				print('WARNING: generic String List example generated, example missing from spec in ' + fieldName)
				arr = [fieldName + '1', fieldName + '2']
			elif (itemSchema['type'] == 'int'):
				print('WARNING: generic Int List example generated, example missing from spec in ' + fieldName)
				arr = [1, 2]
			elif (itemSchema['type'] == 'array'):
				arr.append(buildArrayExample(fieldName, itemSchema))
			elif (itemSchema['type'] == 'object'):
				arr.append(buildObjectExample(itemSchema))
		elif ('properties' in itemSchema):
			arr.append(buildObjectExample(itemSchema))
		
	return arr

def buildObjectExample(schema):
	example = {}
	
	if ('example' in schema):
		example = schema['example']
	elif ('properties' in schema):
		for fieldName in schema['properties']:
			fieldObj = schema['properties'][fieldName]
			
			if ('example' in fieldObj):
				example[fieldName] = fieldObj['example']
			elif ('type' in fieldObj):
				if (fieldObj['type'] == 'string'):
					example[fieldName] = buildStringExample(fieldName, fieldObj)
				elif (fieldObj['type'] == 'integer'):
					example[fieldName] = 0
					print('WARNING: generic Int example generated, example missing from spec in ' + fieldName)
				elif (fieldObj['type'] == 'array'):
					example[fieldName] = buildArrayExample(fieldName, fieldObj)
				elif (fieldObj['type'] == 'object'):
					example[fieldName] = buildObjectExample(fieldObj)
			elif ('properties' in fieldObj):
				example[fieldName] = buildObjectExample(fieldObj)
			
	return example

def buildGroupTitle(callPath, method, callsStrings):
	groupTitles = callsStrings.keys()
	groupTitle = callPath + ' ' + method
	if groupTitle not in groupTitles:
		groupTitleStr = '\n## '
		groupTitleStr += method.capitalize() + ' - ' + re.sub('{.*}', '{ID}', callPath)
		groupTitleStr += ' [/brapi/v2/' + callPath + '] \n'
		
		callsStrings[groupTitle] = {'titleStr': '', 'depReadMeStrings': [], 'readMeStrings': []}
	
	return groupTitle

uniquePaths = []
def buildTitleStr(path, method, params = [], deprecated = False):

	titleStr = '\n### ' 
	if deprecated:
		titleStr += '**Deprecated** '
		
	titleStr += method.capitalize() + ' - ' + path
	
	uniquePathStr = ' /brapi/v2' + path
	for param in params:
		if param['in'] == 'query' :
			uniquePathStr += '{?' + param['name'] + '}'
	
	if uniquePathStr in uniquePaths:
		uniquePathStr += '/'
	uniquePaths.append(uniquePathStr)
	
	titleStr += ' [' + method.upper() + uniquePathStr + ']\n\n'
	
	return titleStr


def buildParametersList(params):
	parametersStr = ' \n\n+ Parameters\n'
	for param in params:
		parametersStr += '    + ' + param['name'] 
		
		if ('required' in param) : 
			parametersStr += ' (Required, ' if param['required'] else ' (Optional, '
		else:
			parametersStr += ' (Optional, '
		
		parametersStr += param['type'] + ') ... ' if 'type' in param else ') ... '
		parametersStr += re.sub(r'\n', '', param['description']) if 'description' in param else ''
		parametersStr += '\n'
	
	return parametersStr


def buildRequestBody(requestBody):
	requestBodyStr = ''
	if 'content' in requestBody:
		if 'application/json' in requestBody['content']:
			if 'schema' in requestBody['content']['application/json']:
				schema = requestBody['content']['application/json']['schema']
				example = ''
				
				if 'type' in schema:
					if 'object' == schema['type']:
						example = buildObjectExample(schema)
					elif 'array' == schema['type']:
						example = buildArrayExample('request', schema)
		
				requestBodyStr += ' \n+ Request (application/json)\n```\n' 
				requestBodyStr += json.dumps(example, indent=4, separators=(',', ': '), default=str, sort_keys=True) 
				requestBodyStr += '\n```\n\n'
	return requestBodyStr


def buildExamples(responses):
	readMeStr = ''
	for code in sorted(responses.keys()):
		if 'content' in responses[code]:
			for type in sorted(responses[code]['content']):
				if 'example' in responses[code]['content'][type]:
					example = responses[code]['content'][type]['example']
				elif 'schema' in responses[code]['content'][type]:
					schema = responses[code]['content'][type]['schema']
					example = buildObjectExample(schema)
				else:
					example = {}
					
				readMeStr += '+ Response ' + code + ' (' + type + ')\n```\n'
				readMeStr += json.dumps(example, indent=4, separators=(',', ': '), default=str, sort_keys=True)
				readMeStr += '\n```\n\n'
	
	return readMeStr

def buildRequestDefTable(obj):
	table = ''
	if 'content' in obj:
		if 'application/json' in obj['content']:
			if 'schema' in obj['content']['application/json']:
				table += '**Request Fields** \n\n'
				table += '<table>\n'
				table += '<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> \n'
				schema = obj['content']['application/json']['schema']
				table += buildObjectTableRow(schema)
				table += '</table>\n'
	return table

def buildResponseDefTable(responses):
	table = ''
	if '200' in responses:
		if 'content' in responses['200']:
			if 'application/json' in responses['200']['content']:
				if 'schema' in responses['200']['content']['application/json']:
					if 'properties' in responses['200']['content']['application/json']['schema']:
						if 'result' in responses['200']['content']['application/json']['schema']['properties']:
							table += '**Response Fields** \n\n'
							table += '<table>\n'
							table += '<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> \n'
							schema = responses['200']['content']['application/json']['schema']['properties']['result']
							table += buildObjectTableRow(schema)
							table += '</table>\n'
	return table

def buildObjectTableRow(schema, parentPrefix = ''):
	row = ''
	if 'properties' in schema:
		requiredProps = []
		if 'required' in schema:
			requiredProps = schema['required']
			
		properties = list(set(schema['properties'].keys()) - set(requiredProps))
		properties = sorted(requiredProps) + sorted(properties)
		
		if len(properties) == 1 and 'data' in properties:
			row += buildObjectTableRow(schema['properties']['data'], parentPrefix)
		else:
			for prop in properties:
				#print(prop)
				#print(schema['properties'][prop].keys())
				
				type = ''
				desc = ''
				
				if 'type' in schema['properties'][prop]:
					type = schema['properties'][prop]['type']
					if 'format' in schema['properties'][prop]:
						type += '<br>(' + schema['properties'][prop]['format'] + ')'
				if type == 'array' and 'type' in schema['properties'][prop]['items']:
					type += '[' +  schema['properties'][prop]['items']['type'] + ']'
				if prop in requiredProps:
					type += '<br><span style="font-size: smaller; color: red;">(Required)</span>'
				
				if 'description' in schema['properties'][prop]:
					desc = schema['properties'][prop]['description'].replace('\n', ' ').replace('|', '')
				
				field = ''
				nextParentPrefix = ''
				
				if parentPrefix == '':
					field = '<span style="font-weight:bold;">' + prop + '</span>'
					nextParentPrefix = prop
				else:
					field = parentPrefix + '<br><span style="font-weight:bold;margin-left:5px">.' + prop + '</span>'
					nextParentPrefix = parentPrefix + '<br>.' + prop
					
				row += '<tr><td>' + field + '</td><td>' + type + '</td><td>' + desc + '</td></tr>\n'
				
				if type == 'object' and 'properties' in schema['properties'][prop]:
					row += buildObjectTableRow(schema['properties'][prop], nextParentPrefix)
				elif type[:5] == 'array' and 'properties' in schema['properties'][prop]['items']:
					row += buildObjectTableRow(schema['properties'][prop]['items'], nextParentPrefix)
	elif 'items' in schema:
		row += buildObjectTableRow(schema['items'], parentPrefix)
			
	return row

def buildReadMe(dir, fullBrAPI):
	readMeStr = ''
	with open(dir + 'GroupDescription.md', "r") as groupDescFile:
		readMeStr += groupDescFile.read() + '\n\n'
		
	callsStrings = {}
	for filename in sorted(glob.iglob(dir + '/**/*.yaml', recursive=True)):
		fileObj = {}	
		with open(filename, "r") as stream:
			try:
				fileObj = yaml.load(stream)
				stream.close()
			except yaml.YAMLError as exc:
				print(exc)
		
		if 'paths' in fileObj:
			for callPath in sorted(fileObj['paths'].keys()):				
				methods = fullBrAPI['paths'][callPath]
				methodKeys = sorted(fullBrAPI['paths'][callPath].keys())
				for methodKey in methodKeys:
					methodObj = methods[methodKey]
					
					desc = ''
					if 'description' in methodObj:
						desc = methodObj['description']
						
					deprecated = False
					if 'deprecated' in methodObj:
						deprecated = methodObj['deprecated']
					
					params = []
					if 'parameters' in methodObj:
						params = methodObj['parameters']
						
					responses = []
					if 'responses' in methodObj:
						responses = methodObj['responses']
						
					requestBody = {}
					if 'requestBody' in methodObj:
						requestBody = methodObj['requestBody']
					
					
					methodStr = '\n\n'
					methodStr += buildTitleStr(callPath, methodKey, params, deprecated)
					methodStr += desc
					methodStr += '\n\n'
					methodStr += buildRequestDefTable(requestBody)
					methodStr += '\n\n'
					methodStr += buildResponseDefTable(responses)
					methodStr += '\n\n'
					methodStr += buildParametersList(params)
					methodStr += '\n\n'
					methodStr += buildRequestBody(requestBody)
					methodStr += '\n\n'
					methodStr += buildExamples(responses)
					
					groupTitle = buildGroupTitle(callPath, methodKey, callsStrings)
					if deprecated:
						callsStrings[groupTitle]['depReadMeStrings'].append(methodStr)
					else:
						callsStrings[groupTitle]['readMeStrings'].append(methodStr)
				
	for title in sorted(callsStrings.keys()):
		readMeStr += callsStrings[title]['titleStr']
		for callDoc in callsStrings[title]['readMeStrings']:
			readMeStr += callDoc
		for depCallDoc in callsStrings[title]['depReadMeStrings']:
			readMeStr += depCallDoc
	
	return readMeStr
	

def buildReadMes(rootPath, specificPath):
	fullBrAPI = dereferenceAll.dereferenceBrAPI(filePath = rootPath + '/brapi_openapi.yaml')
	
	for dir in glob.iglob(rootPath + specificPath + '/', recursive=False):
		readMeStr = buildReadMe(dir, fullBrAPI)
		fileName = dir + '/README.md'
		with open(fileName, 'w') as outfile:
			outfile.write(readMeStr)
			print("fileName - " + fileName)

rootPath = '.'
specificPath = '**'
if len(sys.argv) > 1 :
	rootPath = sys.argv[1];
if len(sys.argv) > 2 :
	specificPath = sys.argv[2];

buildReadMes(rootPath, specificPath)
	
