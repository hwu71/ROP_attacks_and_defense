#!/usr/bin/python
#encoding=utf-8
import sys
import getopt
import os
import datetime

#使用模板方法模式
class Method:
	tab=''
	def __init__(self,src_code,lineNum,func,mode):
		self.src_code = src_code
		self.lineNum = lineNum
		self.func = func
		self.mode = mode
		
	def instrumentTemplate(self):
		line_Str = self.src_code[self.lineNum-1]
		#tab=''
		#print line_Str
		#tab is the string of \t in front of per line,for alignment
		for i in line_Str:
			if i == '\t':
				self.tab+=i
			if i == ' ':
				self.tab+=i
			else:
				break
		#print tab
		#print line_Str
		line_Str1 = line_Str.strip() #去掉每行头尾空白 
		line_Str2 = line_Str1.replace(' ','')
		#eg: strcpy(a,b)
		print self.func
		#print line_Str2
		if (self.func!="Array bound") and (self.func not in line_Str2):
			print "funcName in report_BO.txt does not equal to funcName in source code!"
			return None	
		

		self.src_code.insert(self.lineNum-1,self.tab+'if('+self.repairMethod(self.splitParameters(line_Str2),self.mode)+'){\n'\
		+self.tab+'\tprintf("'+self.func+' may have a buffer overflow, we just exit\\n");\n'+self.tab+'\treturn 0;\n'+self.tab+'}\n')
		return self.src_code
	
	def splitParameters(self,line_Str):
		return None
		
	def repairMethod(self,dest_src,mode):
		codition = None
		return condition
		
class MethodStrcpy(Method):
	#func=''
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str.split(self.func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		dest,src = para2.split(',')
		return [dest,src] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		src = dest_src[1]
		condition=''
		condition = 'strlen('+src+') >= sizeof('+dest+')'
		return condition
		
class MethodStrncpy(Method):
	#eg: strncpy(a,b,n)
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str2.split(func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		dest,src,n = para2.split(',')
		return [dest,n] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		n = dest_src[1]
		condition = n+' > sizeof('+dest+')'
		return condition
		
class MethodStrcat(Method):
	#func=''
	#eg: strcat(a,b)
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str.split(self.func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		dest,src = para2.split(',')
		return [dest,src] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		src = dest_src[1]
		condition=''
		condition = 'strlen('+src+')+strlen('+dest+') >= sizeof('+dest+')'
		return condition
		
class MethodStrncat(Method):
	#eg: strncat(a,b,n)
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str.split(self.func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		dest,src,n = para2.split(',')
		return [dest,src,n] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		src = dest_src[1]
		n = dest_src[2]
		condition = '(strlen('+src+')<='+n+' ? strlen('+src+') : '+n+')+strlen('+dest+') >= sizeof('+dest+')'
		return condition
		
class MethodRead(Method):
	#eg: ssize_t read(int fd, void *buf, size_t count);
	#count > size(buf)
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str.split(self.func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		fd,dest,count = para2.split(',')
		return [dest,count] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		count = dest_src[1]
		condition = count+' > sizeof('+dest+')'
		return condition
		
class MethodFread(Method):
	#eg: size_t fread ( void * ptr, size_t size, size_t count, FILE * stream );
	#size*count > size(ptr)
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str.split(self.func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		dest,size,count,stream = para2.split(',')
		return [dest,size,count] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		size = dest_src[1]
		count = dest_src[2]
		condition = size*count+' > sizeof('+dest+')'
		return condition
		
class MethodFgets(Method):
	#eg: char * fgets ( char * str, int num, FILE * stream );
	#num > size(str)
	def __init__(self,src_code,lineNum,func,mode):
		Method.__init__(self,src_code,lineNum,func,mode)
		
	def splitParameters(self,line_Str):
		para = line_Str.split(self.func)[1]
		para1 = para.split(')')[0]
		para2 = para1.split('(')[1]
		dest,n,stream = para2.split(',')
		return [dest,n] 
		
	def repairMethod(self,dest_src,mode):
		#Method.repairMethod()
		dest = dest_src[0]
		n = dest_src[1]
		condition = n+' > sizeof('+dest+')'
		return condition
		
														
#使用工厂模式
class FuncRepairMethodFactory:
	#def __init__(self):
	function = {'strcpy':MethodStrcpy,'strncpy':MethodStrncpy,'strcat':MethodStrcat,\
	'strncat':MethodStrncat,'read':MethodRead,'fread':MethodFread,'fgets':MethodFgets}	
	def createMethod(self,src_code,lineNum,func,mode):
		method = self.function.get(func)(src_code,lineNum,func,mode)
		return method
#使用单例模式
class Singleton(object):
	def __new__(cls, *args, **kw):
		#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回  
		#如果cls._instance不为None,直接返回cls._instance
		if not hasattr(cls, '_instance'):
			orig = super(Singleton, cls)
			cls._instance = orig.__new__(cls, *args, **kw)
		return cls._instance
					
class Repair(Singleton):
	BO_position = []
	
	def __init__(self,mode):
		self.mode = mode
		self.BO_position = read_report_BO_txt()
	def repair(self):
		fac = FuncRepairMethodFactory()
			
		if self.BO_position == None:
			return 0
		fileLine={}
		#fileLine eg: {'src.c': ['12', '11']}
		file_line_func={}
		#file_line_func eg: {'src_12': 'strcpy'}
		
		for BO_position_i in self.BO_position:
			#eg: src.c_12 strcat
			#eg: src.c_8 Array bound
			file_line,func = BO_position_i.split('\n')[0].split(' ',1)
			file_line_func[file_line] = [func]
			fileName,line = file_line.split('_')
			if fileLine.get(fileName) == None:
				fileLine[fileName] = [int(line)]
			else:
				fileLine[fileName].append(int(line))
		#print fileLine
		print file_line_func
		
		for key in fileLine.keys():
			#print fileLine[key]	
			#倒序插装
			#eg: we first instrument line 14,then instrument line 12,in case of after instrument,
			#the line NUM after that instrument will change
			fileLine[key].sort(reverse=True)
			#print fileLine[key]
		print fileLine	
		
		for key in fileLine.keys():
			f = open(key)
			src_code = f.readlines()
			f.close()
			for line in fileLine[key]:
				funcName = file_line_func[key+'_'+str(line)][0]	
				funcMethod = fac.createMethod(src_code,line,funcName,self.mode)
				src_code = funcMethod.instrumentTemplate()
				if src_code == None:
					return 0
			f2 = open(key,'w')
			f2.writelines(src_code)
			f2.close()
		return 1
		
def read_report_BO_txt():
	#contents: src.c_12 strcpy\n
	if os.path.exists('report_BO.txt')==False:
		print "report_BO.txt doesn't exist"
		return None
	f = open('report_BO.txt')
	try:
		lines = f.readlines()
		print lines
	finally:
		f.close()
	return lines
	
def Usage():
	print 'buffer overflow repair instrument.py usage:'
	print 'Input file needed: src.c,report_BO.txt'
	print 'Output file: src.c(repaired)'
	print '-h,--help: print help message.'
	return 0
		
def main(argv):
	try:
		opts, args = getopt.getopt(argv[1:],'h:',['help'])
	except getopt.GetoptError, err:
		print str(err)
		Usage()
		sys.exit(2)
	#print opts
	if opts == []:
		starttime = datetime.datetime.now()
		repairObject = Repair('default')
		res = repairObject.repair()
		if res == 0:
			print "An error occured when instrument!"
		endtime = datetime.datetime.now()
		print "Total time:",(endtime - starttime).seconds,"second(s)."
		sys.exit(0)
	for o,a in opts:
		if o in('-h','--help'):
			Usage()
			sys.exit(1)
		else:
			print 'unhandled option'
			sys.exit(3)

	#return 0
	
if __name__ == "__main__":
    main(sys.argv)