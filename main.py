import pytest
import subprocess
import settings
import multiprocessing

ALLURE_FILE = settings.ALLURE_FILE


# 方法1，只能执行全部的测试用例以及执行完后会生成 Allure 原始结果在 result/ 目录
# if __name__ == "__main__":
# cpu_count = multiprocessing.cpu_count()
#     pytest.main([
#         "-n", str(cpu_count),
#          # 重复执行用例
#         "--count=1",
#         # 失败用例重跑
#         "--reruns=3",
#         # 重跑间隔时间
#         "--reruns-delay=1",
#         # 生成 Allure 原始结果在 result/ 目录
#         "--alluredir=result",
#         # 跳过指定用例
#         "-k", "not test_05",
#         # 跳过指定py文件
#         "--ignore=testcase/test_demo1.py"
#     ])

# 方法2 只能执行全部的测试用例以及生成allure测试报告自动打开报告


def run_tests():
    # multiprocessing自动获取CPU核心数
    cpu_count = multiprocessing.cpu_count()
    pytest.main([
        "-v",
        # 自动根据 CPU 数量设置并发进程数,xdist分布式执行
        "-n", str(cpu_count),
        # 重复执行用例
        "--count=1",
        # 失败用例重跑
        "--reruns=3",
        # 重跑间隔时间
        "--reruns-delay=1",
        # 生成 Allure 原始结果在 result/ 目录
        "--alluredir=result",
        # 跳过指定用例
        "-k", "not test_05",
        # 跳过指定py文件
        # "--ignore=testcase/test_demo1.py"
    ])
    subprocess.run([ALLURE_FILE, "generate", "result", "-o", "report", "--clean"])
    subprocess.run([ALLURE_FILE, "open", "report"])


if __name__ == "__main__":
    run_tests()
