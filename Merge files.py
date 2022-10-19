import os
import shutil


def walkFile(file):
    successful_file = 0
    failure_file = []
    for root, dirs, files in os.walk(file):
        # 遍历文件
        for f in files:
            fileName = os.path.join(root, f)
            # 获取文件后缀为.m3u8
            if str(os.path.splitext(fileName)[-1]) == ".m3u8":
                name = os.path.splitext(fileName)[0]
                Path = os.path.abspath(os.path.join(name, "../"))
                cmd = rf'ffmpeg.exe -allowed_extensions ALL -protocol_whitelist "file,http,crypto,tcp" -i {fileName} -c copy {Path.split("m3u8")[0]}'
                # 执行合并命令
                os.system(cmd)
                successful_file += 1
                # 判断文件是否合并，合并完成后删除文件
                if os.path.exists(Path.split("m3u8")[0]) == True:
                    shutil.rmtree(Path)
                else:
                    failure_file.append(Path.split("m3u8")[0])
                    f = open("err.txt", "a",encoding="utf-8")
                    f.write(Path.split("m3u8")[0])
                    f.write("\n")
                    f.close()

    return f'合并文件完成，共合并{successful_file}个文件，其中成功：{successful_file - len(failure_file)} 个文件， 失败：{len(failure_file)} 个文件，失败文件请查看err文件'


if __name__ == '__main__':
    print(walkFile("./download"))
