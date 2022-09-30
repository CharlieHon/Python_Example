# 导入argparse包
import argparse

def main():
    # 使用ArgumentParser类生成一个parser对象(参数解析器)，description描述这个参数解析器作用
    parser = argparse.ArgumentParser(description="Dome of argparse")
    # 通过对象的add_argument函数增加参数，这里增加了两个参数name和year
    # 其中`-n`, `--name`表示同一个参数，default参数表示在命令行没有提供参数时提供的默认值
    # 当'-', '--'同时出现时，系统默认后者为参数名，前者不是，但是在命令行输入时不区分
    parser.add_argument('-n', '--name', default='Han')
    parser.add_argument('-y', '--year', default='2022')
    # 采用对象的parse_args获取解析器的参数，Namespace中有两个属性/成员
    args = parser.parse_args()
    print(args)
    name = args.name
    year = args.year
    print('Hello {} {}'.format(name, year))


if __name__ == '__main__':
    main()