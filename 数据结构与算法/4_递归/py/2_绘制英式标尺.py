'''
绘制英式标尺，递归实现(p97)
    函数1：draw_ruler管理整个标尺的构建
        参数1：num_inches，标尺的总长度
        参数2：major_length，主刻度线的长度
    函数2：draw_line
        参数1：tick_length，刻度线的长度
        参数2：tick_lable，刻度标签
        功能1：用指定数量的破折线绘制一个单独的刻度线
        功能2：在刻度线之后打印一个相应的刻度标签
    函数3：draw_interval，用于递归的执行任务
        参数1：center_length，相对位置处于中间的刻度线的长度
        功能1：若center_length >= 1，则操作的第一步和最后一步调用      draw_interval(center_length-1)，中间步骤则是           draw_line(center_length)绘制一次刻度线
        功能2：若center_length = 0，则不绘制任何东西
'''
def draw_ruler(num_inches,major_length):
    draw_line(major_length,'0')
    for j in range(1,1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))

def draw_line(tick_length,tick_lable=' '):
    line='-'*tick_length
    if tick_lable:
        line+=' '+tick_lable
        print(line)

def draw_interval(center_length):
    if center_length>0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)

draw_ruler(2,4)