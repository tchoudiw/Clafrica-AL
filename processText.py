# coding: utf-8 
'''
Created on 2017-01-21
This section provide Class ProcessText with methods for the string treatment for replacement code purpose with the special characters
@author: Wiliam Tchoudi
'''
import re  # regular expression Mod le

class ProcessText(object):
    '''
    This Class define all methods using for replacing clafrica code in the the text typed from Keyboard.
    The replacement use the clafrica keys values from a literal object as a source regardless to order of the keys
    '''
    '''Many Regular expressions patern  '''
    __tabReg = [ "\.\.([b-df-z\?]|ai|af|eu)|ai1_|ai2_|eu1_|af1_|uu1_|o\*1_|e1_|e3_|a1_|a2_|o1_|e_|(af|eu|o\*|uu|n\*|N\*)[2357]|(ii)[157]|(ai)[357]|(n\*|N\*)[1]|[AmMnNO][12357]|(c)[157]|(s)[57]|h1|e[257]|a[357]|[o][2357]|b\*|d\*|\*n|D\*|B\* |\*N",    
                   "\.\.e|\.\.a|\.([b-z\?]|ai|af|eu)|u1_|i1_|[iu][357]|u2|e1|e3|a1|a2|o1|ai2|(ai|eu|af|o\*|uu)1|n\*",
                  "\.e|\.a|i[12]|u1|ai|ii|eu|af|uu|o\*"]

    def __init__(self, allClafricaCode):
        '''
        Constructor
        '''
        self.allClafricaCode = allClafricaCode
    
            
    '''Method that check and return the right code to be replaced taking in account
     the regular expression and post fix matter for a subcode include in another code 
     @param strTyped : string 
     @return: vCode, string
     '''   
    def setCode(self,strTyped):
        vCode=""
        ln = len(self.__tabReg)
        for i in range(0,ln):
            tcod1 = re.search(self.__tabReg[i], strTyped, re.M) 
            if tcod1:
                vCode = tcod1.group()   
                return vCode 
        return vCode 
        
    ''' Method to replace the rigth clafrica code in the typed text 
        @param param: strClip, sting
        @param param: initCode, sting
        @return: strClip, sting
        '''   
    def replaceCode(self,strClip,initCode):
        vClafValue = ""
        vStrClip = strClip
        vCode = self.setCode(vStrClip)
        while( len(vCode) > 0):
            vClafValue = self.allClafricaCode[vCode]
            vStrClip = vStrClip.replace(vCode, vClafValue)
            vCode = self.setCode(vStrClip)
            
        return vStrClip
    
    
    ''' Method that return the text string translated after replacing the clafrica key code by thier values if necessary
        @param pCodeStr: string  
        @return: translatedStr, string'''
    def getTranlate(self,strToTranslate):
        translatedStr = strToTranslate
        scode = ""
        for key, value in self.allClafricaCode.items():
            scode+= key
            #print(key)
            findCode = translatedStr.find(key)
            if (findCode > -1):
                translatedStr = self.replaceCode(translatedStr, key)
                #break
        return translatedStr      
    
#end