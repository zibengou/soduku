from numpy import *
import math
# 读取文本中数独数据
def sodukuArray(path):
	fi = open(path,'r')
	out = fi.read()
	fi.close()
	out = out.replace("\n","")
	resultList = []
	for ou in out.split(";"):
		strList = array(list(ou.replace('\n','').replace(',','')))
		if len(strList) < 1:
			continue
		intList = strList.astype(int)
		# resultList.append(intList.reshape(9,9))
		resultList.append(intList)
	return resultList

#已知数独阵转为精确覆盖阵
def sodukuToRect(soduku):
	position = 0
	rect = []
	for num in soduku:
		if num == 0:
			position = position + 1
			continue
		pRow = int(position / 9)
		pCol = position % 9
		row = pRow*9 + num
		col = pCol*9 +num
		pGon = ((pRow % 3 * 3) + (int(pCol/3) % 3) + 1)*9+num
		res = (position+1,row,col,pGon)
		rect.append(res)
		position = position+1
	return rect

#完整数独精确覆盖阵729行，324列
def coverArray():
	# zeroPosition = identity(81)
	# zeroRow = identity(81)
	# zeroCol = identity(81,int)
	# zeroGon = identity(81)
	# for i in range(math.factorial(9)**9):
	# 	print(1)
	rowList = []
	colList = []
	positionList = []
	rect = []
	for position in range(81):
		pRow = int(position / 9)
		pCol = position % 9
		for num in range(9):
			num = num + 1
			row = pRow*9 + num
			col = pCol*9 +num
			# if row in rowList or col in colList:
			# 	continue
			# colList.append(col)
			# rowList.append(row)
			# positionList.append(position)
			pGon = ((pRow % 3 * 3) + (int(pCol/3) % 3))*9+num
			res = (position+1,row,col,pGon)
			rect.append(res)
	return rect

#去重算法，非迭代
def removeImpossible(testRect, rect):
	newRect = [i for i in rect]
	for line in rect:
		remove = 0
		for testLine in testRect:
			if testLine[0] == line[0] or testLine[1] == line[1] or testLine[2] == line[2] or testLine[3] == line[3]:
				newRect.remove(line)
				break
	noConflictNumList = [i for i in newRect]
	for i in range(len(newRect)):
		for j in range(i+1,len(newRect)):
			iline = newRect[i]
			jline = newRect[j]
			if iline[0] == jline[0] or iline[1] == jline[1] or iline[2] == jline[2] or iline[3] == jline[3]:
				if iline in noConflictNumList:
					noConflictNumList.remove(iline)
				if jline in noConflictNumList:
					noConflictNumList.remove(jline)
				break
	newTestRect = [i for i in testRect] + noConflictNumList
	for i in noConflictNumList:
		newRect.remove(i)
	return(newTestRect, newRect)

#测试迭代算法，未完成
def singleFind(testRect,rect):
	(newTestRect, newRect) = removeImpossible(testRect,rect)
	print(1)
	if len(testRect) < 81 and not len(newTestRect) == len(testRect):
		return singleFind(newTestRect,newRect)
	else:
		return (newRect, newTestRect)

if __name__=='__main__':
	rect = coverArray()
	testsoduku = sodukuArray('soduku.txt')[0]
	testRect = sodukuToRect(testsoduku)
	(resultTest,resultTestRect) = singleFind(testRect,rect)
	print(len(resultTestRect))