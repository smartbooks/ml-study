#coding:utf-8

import sys
sys.coinit_flags = 0

import win32gui
import win32api
import win32con
import pythoncom
import win32com
import win32com.client

#spyxx.exe
#Chrome
#p1 = win32gui.FindWindow("CefWebViewWnd", "微信")
#p2 = win32gui.FindWindowEx(p1,0,"CefBrowserWindow","")
#p3 = win32gui.FindWindowEx(p2,0,"Chrome_WidgetWin_0","")
#p4 = win32gui.FindWindowEx(p3,0,"Chrome_RenderWidgetHostHWND","Chrome Legacy Window")

##IE,只能在IE版本下调试通过,Chrome下不行
p0 = win32gui.FindWindow("IEWebViewWnd", "微信")
p1 = win32gui.FindWindowEx(p0, 0, "ActiveXWnd","UIActiveX")
p2 = win32gui.FindWindowEx(p1, 0, "Shell Embedding","")
p3 = win32gui.FindWindowEx(p2, 0, "Shell DocObject View","")
p4 = win32gui.FindWindowEx(p3, 0, "Internet Explorer_Server","")

print("p0=",p0,"p1=",p1,"p2=",p2,"p3=",p3,"p4=",p4)

msg = win32gui.RegisterWindowMessage('WM_HTML_GETOBJECT')
ret, result = win32gui.SendMessageTimeout(p4, msg, 0, 0, win32con.SMTO_ABORTIFHUNG, 1000)
#result = win32gui.SendMessage(p4, msg, 0, 0)
print("result=",result)

ob = pythoncom.ObjectFromLresult(result, pythoncom.IID_IDispatch, 0)
doc = win32com.client.dynamic.Dispatch(ob)

print("url=",doc.url,"title=",doc.title)
#doc.all['id'].click()
