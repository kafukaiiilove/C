import qrcode

# 公网 IP 和参数模板
base_url = "http://47.122.68.238/redirect"
merchant_id = 2  # 商家ID，可以根据需要修改
merchant_name = "嘻嘻嘻"  # 商家名称

# 构建 URL
url = f"{base_url}?id={merchant_id}&name={merchant_name}"

# 生成二维码
img = qrcode.make(url)
img.save(f"shangjia{merchant_id}.png")  # 保存为 shangjia1.png 或 shangjia2.png

print(f"二维码已保存为 shangjia{merchant_id}.png")
