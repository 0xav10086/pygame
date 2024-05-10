import json
import os

# 文件夹路径
folder_path = '/1999/yolo/dataset'

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def get_bbox_from_polygon(polygon_points):
    min_x = min(point[0] for point in polygon_points)
    max_x = max(point[0] for point in polygon_points)
    min_y = min(point[1] for point in polygon_points)
    max_y = max(point[1] for point in polygon_points)
    return [min_x, min_y, max_x, max_y]

def main():
    # 遍历文件夹中的所有JSON文件
    for json_file in os.listdir(folder_path):
        if json_file.endswith('.json'):
            json_path = os.path.join(folder_path, json_file)
            # 读取JSON文件数据
            with open(json_path, 'r') as load_f:
                content = json.load(load_f)
            # 循环处理每个标注
            for shape in content['shapes']:  # 假设标注在'shapes'键下
                points = shape['points']
                # 检查标注类型，如果是多边形，则计算矩形边界框
                if len(points) > 2:  # 多边形标注
                    bbox = get_bbox_from_polygon(points)
                else:  # 矩形标注
                    bbox = [points[0][0], points[0][1], points[1][0], points[1][1]]
                # 计算YOLO格式所需的中心点坐标和宽高
                x, y, w, h = convert((content['imageWidth'], content['imageHeight']), bbox)
                # 构建TXT文件内容
                file_str = f"{shape['label']} {x} {y} {w} {h}"
                # 写入对应的TXT文件
                txt_filename = json_file.replace('.json', '.txt')
                with open(os.path.join(folder_path, txt_filename), 'a') as file:
                    file.write(file_str + '\n')

if __name__ == '__main__':
    main()
