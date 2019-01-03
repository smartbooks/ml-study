
package com.ljja.mlstudy.helper

import java.io.{PrintWriter, StringWriter}

/**
  * 用法示例:
  * ThrowablePrint.printStackTrace(e)
  */
object ThrowablePrint {

  private val charset = "UTF-8"

  def getStackTrace(e: Throwable): String = {
    val sw = new StringWriter()
    e.printStackTrace(new PrintWriter(sw))
    sw.toString
  }

  def printStackTrace(e: Throwable): Unit = {
    printStackTrace("", e)
  }

  def printStackTrace(tag: String, ex: Throwable): Unit = {

    val motd =
      """
        |                   _ooOoo_
        |                  o8888888o
        |                  88" . "88
        |                  (| -_- |)
        |                  O\  =  /O
        |               ____/`---'\____
        |             .'  \\|     |//  `.
        |            /  \\|||  :  |||//  \
        |           /  _||||| -:- |||||-  \
        |           |   | \\\  -  /// |   |
        |           | \_|  ''\---/''  |   |
        |           \  .-\__  `-`  ___/-. /
        |         ___`. .'  /--.--\  `. . __
        |      ."" '<  `.___\_<|>_/___.'  >'"".
        |     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
        |     \  \ `-.   \_ __\ /__ _/   .-` /  /
        |======`-.____`-.___\_____/___.-`____.-'======
        |                   `=---='
        |
        |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        |           佛祖保佑       永无BUG
      """.stripMargin

    println(motd)

    println("==========Exception Start============================")

    println(s"TAG:${tag}")

    println(s"异常消息:${ex.getMessage}")

    val stackTrace = getStackTrace(ex)

    println(s"异常堆栈:\n${stackTrace}")

    println("==========Exception End==============================")
  }

}
