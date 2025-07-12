# 项目 1：API 请求限流器
# 描述：实现一个装饰器，限制 API 请求的频率，防止服务器过载

import time

def rate_limiter(max_calls, period):
    """
    限制函数调用频率的装饰器。
    :param max_calls: 每个时间段内允许的最大调用次数。
    :param period: 时间段（秒）。
    """
    calls = []  #存储时间戳的列表（记录每次调用时间）

    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            # 移除超时的调用记录
            #calls[:] = [call for call in calls if now - call < period]
            # 拆解为多行简单代码：
            # 1. 创建临时列表存储有效调用
            valid_calls = []
            # 2. 遍历所有历史调用记录
            for call_time in calls:
                # 3. 计算调用发生至今的时间差
                time_since_call = now - call_time
                # 4. 检查是否在有效时间窗口内
                if time_since_call < period:
                    # 5. 保留有效调用记录
                    valid_calls.append(call_time)
            # 6. 原地更新调用记录列表（保持闭包引用）
            calls.clear()  # 清空原列表
            calls.extend(valid_calls)  # 添加有效记录
            if len(calls) >= max_calls:
                raise Exception("请求频率过高，请稍后再试")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 测试案例
@rate_limiter(max_calls=3, period=5)
def api_request():
    print("API 请求成功")

# 模拟请求
for i in range(5):
    try:
        api_request()
    except Exception as e: #异常处理
        print(e)
    time.sleep(1)
