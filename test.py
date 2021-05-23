import pyupbit

access = "xxTgU8Kx443fckotlyAxPRdCRixfAw0goV6dZ3Xl"          # 본인 값으로 변경
secret = "vMEjUTtxiU0dkxqJXLr2Tdm6UrsW8VCJmK6XdQ5B"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTT"))     # KRW-BTT 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회