#! /usr/bin/env python

import sys
import json
import glob
import yaml
import re
import os

def go():
		
	outPath = './'
	headerPath = './swaggerMetaData.yaml'
	sourcePath = './'
	
	if '-out' in sys.argv:
		i = sys.argv.index('-out')
		outPath = sys.argv[i + 1]
		if outPath[-1] != '/':
			outPath = outPath + '/'
			
	if '-header' in sys.argv:
		i = sys.argv.index('-header')
		headerPath = sys.argv[i + 1]
		
	if '-source' in sys.argv:
		i = sys.argv.index('-source')
		sourcePath = sys.argv[i + 1]
		if sourcePath[-1] != '/':
			sourcePath = sourcePath + '/'
	
	headerHTML = ''
	with open(headerPath, "r") as headerFile:
		try:
			fileObj = yaml.load(headerFile)
			if 'info' in fileObj:
				if 'description' in fileObj['info']:
					headerHTML = parseHTMLToMD(fileObj['info']['description'])
					
		except yaml.YAMLError as exc:
			print(exc)
	
	outFilePath = outPath + 'brapi_blueprint.apib'
	outFileJsonPath = outPath + 'brapi_blueprint.apib.json'
	
	#outREADMEFilePath = outPath + 'README.md'
	#if os.path.exists(outREADMEFilePath):
	#	os.remove(outREADMEFilePath)
	
	sources = glob.glob(sourcePath + '*/README.md', recursive=True)
	sources = sorted(sources)
		
	fullText = headerHTML
	for source in sources:
		source = source.replace('\\', '/')
		print(source)
		with open(source, "r") as inFile:
			filetext = inFile.read()
			fullText += filetext
	
	with open(outFilePath, "w") as outFile:
		outFile.write(fullText)
		print(outFilePath)
		
	with open(outFileJsonPath, "w") as outFileJson:
		jsonWrapper = {'code': fullText}
		json.dump(jsonWrapper, outFileJson)
		print(outFileJsonPath)
		
	#with open(outREADMEFilePath, "w") as outRMFile:
	#	outRMFile.write(fullText)
	#	print(outREADMEFilePath)
			
def parseHTMLToMD(htmlStr):
	title = re.search(r'<div class="[^"]*current-brapi-section[^"]*">\n\s*<h2 class="brapi-section-title">([^<]*)</h2>', htmlStr).group(1)
		
	body = re.sub(r'<h2 class="brapi-section-title">([^<]*)</h2>', r'### \1', htmlStr)
	body = re.sub(r'<div class="brapi-section-description">([^<]*)</div>', r'\1', body)
	body = re.sub(r'<div class="version-number">([^<]*)</div>\n', r'\n\1', body)
	body = re.sub(r'<div class="stop-float"></div>', r'', body)
	body = re.sub(r'<div class="[^"]*brapi-section[^"]*">', r'', body)
	body = re.sub(r'\n\s*</div>', r'\n', body)
	body = re.sub(r'<div class="link-btn"><a.*href="([^"]*)">([^<]*)</a></div>\n', r' - [\2](\1)', body)
	body = re.sub(r'<div class="gen-info-link"><a.*href="([^"]*)">([^<]*)</a></div>', r'- [\2](\1)', body)
	body = re.sub(r'<style>[^<]*</style>', r'\n', body)
	
	body = re.sub(title, '**' + title + '**', body)
	
	mdStr = 'FORMAT: 1A\n\n# ' + title + '\n\n' + body
	
	return mdStr
			
go()