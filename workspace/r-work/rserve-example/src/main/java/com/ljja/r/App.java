package com.ljja.r;

import org.rosuda.REngine.REXP;
import org.rosuda.REngine.Rserve.RConnection;

/*
RServe启动命令:
D:\tool\R-3.4.3\library\Rserve\libs\x64>R CMD Rserve --RS-enable-remote --RS-conf E:/work/github/ml-study/r-work/Rserv.cfg
 */
public class App {

    public static void main(String[] args) {
        try {

            RConnection rcon = new RConnection("localhost", 6311);    //建立远程链接

            String rv = rcon.eval("R.version.string").asString();     //得到R版本信息
            System.out.println(rv);                                   //输出版本信息

            //调用R内置函数
            double[] arr = rcon.eval("rnorm(5)").asDoubles();        //通过R得到10个随机数返回数组

            for (double x : arr)                                         //遍历集合
            {
                System.out.println(x);
            }

            //调用R自定义函数
            //rcon.eval("source(\"E:/work/github/ml-study/r-work/start.R\")");
            REXP rexp = rcon.eval("area(10)");
            System.out.println("面积是:" + rexp.asDouble());

            System.out.println("success");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
