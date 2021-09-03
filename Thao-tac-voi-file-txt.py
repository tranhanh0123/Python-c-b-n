import os
import io

# lấy ra đường dẫn hiện tại đang code
# a = os.getcwd()
# print(a)


#chuyển sang một đường dẫn khác
# a = os.chdir(r"E:\Laptrinhpython\Thao-tac-voi-file-trong-python")
# print(a)


#mở một file. nếu chưa có file sẽ tự tạo
# def mo_file(tenfile):
#     f = open(tenfile,"w")
#     f.close()
# tenfile="vidu.txt"
# mo_file(tenfile)


#đổi tên một file
# def doi_ten_file():
#     f = os.rename("vidu.txt","Testdoiten.txt")
# doi_ten_file()



#xóa một file
# def xoa_file():
#     f = os.remove("Testdoiten.txt")
# xoa_file()



#coppy một file
# from shutil import copyfile
# def coppy_file():
#     f =copyfile("vidu.txt","vidu222.txt")
# coppy_file()



#ghi file ko utf8
# def ghifile(tenfile,noidung):
#     f = open(tenfile,"a")
#     f.write(noidung+'\n')
#     f.close()
# tenfile = "vidu.txt"
# noidung = "con cac"
# ghifile(tenfile,noidung)



#ghi file có tiếng việt (UTF8)
# def ghi_file(filename,nd_line):
#     f = io.open(filename, "a", encoding="utf-8")
#     f.write(nd_line + '\n')
#     f.close()
# filename = "test.txt"
# nd_line = "xin chào cả nhà nhé @@"
# ghi_file(filename,nd_line)



#ghi vào file từ 1 list có sẵn :
# def ghi_file_tu_list(filename,list):
#     f = io.open(filename,"w",encoding="utf-8")
#     f.write("\n".join(list))
#     f.close()
# filename = "test.txt"
# list = ["văn hạnh","Tên gì","học ra sao","văn hạnh"]
# ghi_file_tu_list(filename,list)





#đọc file có utf8 - trả về một danh sách (ko phải list)
# def doc_file():
#     f = io.open("test.txt", mode="r", encoding="utf-8")
#     doc_van_ban = f.readlines()
#     print(doc_van_ban)
#     for i in doc_van_ban:
#         print(i)
# doc_file()

#đọc file có utf8 trả về 1 list
# def doc_file(tenfile):
#     f = io.open(tenfile,mode="r", encoding="utf-8")
#     noi_dung = f.read()
#     f.close()
#     return noi_dung.split("\n")

# tenfile = "test.txt"
# print(doc_file(tenfile))














