""" 
    phân tích và thiết kế giải pháp:
        + Input:
            + giá trị nhập lựa chọn menu 
            + Chức năng 2:
                + Nhập mã sản phẩmn
                + Nhập tên sản phẩm
                + Nhập số lượng sản phẩm
                + Nhập đơn giá của sản phẩm
            + Chức năng 3:
                + Mã sản phẩm 
                + Số lượng cần thay đổi (Nếu tìm thấy mã)
            + Chức năng 4:
                + Mã sản phẩm
        + Output:
            + Chức năng 1: 
                +Danh sách sản phẩm theo định dạng 
            + Chức năng 2: 
                + Thông báo đã thêm sản phẩm hay sản lượng
            + Chức năng 3:
                + Thông báo số lượng thêm thành công
            + Chức năng 4:
                + Thông báo xóa sản phẩm thành công
                
        + Đề xuất giải pháp:
            + Ở phần menu ta sử dụng vòng while với điều kiện True
            + NẾU NGƯỜI DÙNG NHẬP CHỮ CÁI HOẶC NHẬP NGOÀI CHỨC NĂNG 
            => BÁO LỖI CHO CHƯƠNG TRÌNH VÀ CHO NHẬP LẠI 
            + Chức năng 1:
                + Cho người dùng hiện giỏ hàng và tính số tiền
                + Sử dụng for để duyệt trong mảng
            + Chức năng 2:
                + Cho người dùng nhập mã sản phẩm
            + Chức năng 4:
                + Cho người dùng nhập mã 
                => Nếu tìm thấy thì cập nhật lại số lượng
                => Nếu không tìm thấy thì báo lỗi 
            + Chức năng 5: Bye
            
        + Thiết kế thuật toán :
            + Khi vừa vào mình sẽ in ra menu cho người dùng 
                + với mỗi chức năng mình ấn thì mình sẽ thực hiện chức năng tương ứng với 
                người dùng
                + sau khi sử dụng chức năng đó thì cho người dùng quay lại menu 
                và nhập lại đến khi nhập chức năng thoát thì kết thức chương trình
        + BẪY
            + NẾU NGƯỜI DÙNG NHẬP SỐ LƯỢNG < =0 HOẶC GIÁ < 0 
            => HỆ THÔNG BÁO LỖI VÀ KHÔNG THỰC HIỆN THAO TÁC CHO NGƯỜI DÙNG NHẬP LẠI
            + BẪY 2: NẾU NHẬP MÃ SẢN PHẨM KHÔNG CÓ TRONG GIỎ THÌ TA SẼ THÔNG BÁO
            => KHÔNG CÓ SẢN PHẨM TỒN TẠI TRONG HÀNG VÀ CHO NGƯỜI DÙNG NHẬP LẠI
            + BẪY 3: NẾU NGƯỜI DÙNG NHẬP SAI CHỨC NĂNG NGOÀI VÙNG CÙNG NHƯ NHẬP CHỮ CÁI
            => THÔNG BÁO PHẢI THUỘC TỪ 1- > 5  
            
"""

cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]
LINE = "="*60
import time 
while True:
    try: 
        choose = int(input(
        f"{LINE}\n"
        f"{"SHOPEE CART MANAGEMENT SYSTEM".center(60, " ")} \n"
        f"{LINE}\n"
        f"{"[1]. Xem chi tiết giỏ hàng & tính tổng tiền".ljust(60, " ")} \n"
        f"{"[2]. Thêm sản phẩm mới / Cộng dồn số lượng".ljust(60, " ")} \n"
        f"{"[3]. Cập nhật số lượng của một sản phẩm".ljust(60, " ")} \n"
        f"{"[4]. Xóa sản phẩm khỏi giỏ hàng".ljust(60, " ")} \n"
        f"{"[5]. Thoát chương trình".ljust(60, " ")} \n"
        f"{LINE}\n"
        f"> Lựa chọn chức năng: "        
        ))
    except:
        print("Lỗi nhập không khớp với dữ liệu")
        continue 
    match choose:
        case 1:
            total_quantity = 0
            total_money = 0
            print()
            print(
                f"{"CHI TIẾT GIỎ HÀNG".center(105, "-")}\n"
                f"{"STT":<5} | {"MÃ SP":<10} | {"Tên Sản Phẩm":<30} | {"SL":<5} | {"Đơn Giá":<20} | {"Thành tiền":<20}\n"
                f"{"".center(105, "-")}\n"
                )
            for index, value in enumerate(cart_items):
                print(f"{index + 1:<5} | {value[0]:<10} | {value[1]:<30} | { value[2]:<5} | {f"{value[3]:,}đ":<20} | {f"{(value[3] * value[2]):,}đ":<20}")
                total_quantity += value[2]
                total_money += (value[3] * value[2])
            print("".center(105, "-"))
            print(
                f"=> Tổng số lượng sản phẩm trong giỏ: {total_quantity} \n"
                f"=> TỔNG TIỀN THANH TOÁN: {total_money:,} đ\n"
            )
            print()
        case 2:
            print()
            print("=== THÊM MỚI SẢN PHẨM ===")
            while True:
                product_code = input("Vui lòng nhập mã sản phẩm: ").strip().upper()
                if(not product_code.strip()):
                    print("Mã sản phẩm không được để trống")
                    continue 
                break 
            found = False
            up_index = -1 
            for index, item in enumerate(cart_items):
                if(item[0] == product_code):
                    found = True
                    up_index = index
                    break
            if not found:
                print("=== THÊM SẢN PHẨM MỚI ===")
                while True:
                    product_name = input("Vui lòng nhập tên sản phẩm: ").strip().title()
                    if(not product_name.strip()):
                        print("Tên sản phẩm không được để trống !")
                        continue 
                    break 
                while True:
                    try:
                        product_quantity = int(input("Vui lòng nhập số lượng của sản phẩm: "))
                    except:
                        print("Số lượng sản phẩm không hợp lệ !")
                        continue 
                    if(product_quantity < 0 ):
                        print("Số lượng sản phẩm không được dưới 0")
                        continue 
                    break 
                while True:
                    try:
                        unit_price = int(input("Vui lòng nhập đơn giá của sản phẩm: "))
                    except:
                        print("Đơn giá không hợp lệ !")
                        continue 
                    
                    if(unit_price < 0):
                        print("Đơn giá không được nhỏ hơn 0 !")
                        continue 
                    break 
                current_data = [product_code, product_name, product_quantity, unit_price]
                cart_items.append(current_data)
                print("Đã thêm sản phẩm thành công !")
            else:
                print(f"Sản phẩm mã {product_code} đã tồn tại !")
                while True:
                    try:
                        product_quantity = int(input("Vui lòng nhập số lượng của sản phẩm: "))
                    except:
                        print("Số lượng sản phẩm không hợp lệ !")
                        continue 
                    if(product_quantity < 0 ):
                        print("Số lượng sản phẩm không được dưới 0")
                        continue 
                    break 
                cart_items[index][2] += product_quantity
                print("Đã thêm số lượng thành công !")
            
            print()
        case 3:
            print()
            while True:
                product_wanna_change = input("Vui lòng nhập mã sản phẩm mà bạn muốn cập nhật: ").strip().upper()
                if(not product_wanna_change.strip()):
                    print("Mã sản phẩm không được để trống !")
                    continue 
                break
            
            update_index = -1
            for index, item in enumerate(cart_items):
                if(item[0] == product_wanna_change):                    
                    update_index = index 
                    break 
            
            if(update_index == -1):
                print("Mã sản phẩm của mình không có trong mảng !")
            else:
                while True:
                    try:
                        quantity_to_change = int(input("Vui lòng nhập số lượng sản phẩm muốn thay đổi: "))
                    except:
                        print("Số lượng thay đổi không phù hợp !")
                        continue 
                    if(quantity_to_change < 0):
                        print("Số lượng thay đổi không được nhỏ hơn 0 !")
                        continue 
                    break 
                
                cart_items[index][2] = quantity_to_change 
                print(f"Thay đổi số lượng của sản phẩm mã {product_wanna_change}")
            
            print()
        case 4:
            print()
            while True:
                product_wanna_delete = input("Vui lòng nhập mã sản phẩm mà bạn muốn xóa: ").strip().upper()
                if(not product_wanna_delete.strip()):
                    print("Mã sản phẩm không được để trống !")
                    continue 
                break
            del_index = -1
            for index, item in enumerate(cart_items):
                if(item[0] == product_wanna_delete):
                    del_index = index 
                    break 
            if(del_index == -1):
                print("Mã sản phẩm của mình không có trong mảng !")
            else:
                del cart_items[del_index]
                print(f"Xóa thành công sản phẩm mã {product_wanna_delete}")
            print()
        case 5:
            print()
            message = "Tạm biệt, Chương trình sẽ hủy ngay sau: "
            for letter in message:
                print(letter, end = "", flush=True)
                time.sleep(0.09)
            count = 5
            print()
            time.sleep(0.05)
            while count > 0:
                print(count, end = "\r")
                time.sleep(1)
                count -= 1
            print("BYE :>")
            break
        case _:
            print("Không có chức năng này !")
