# Copyright 2020 Erwin Lejeune ; Sampreet Sarkar
# Under MIT Licence

import rclpy
from rclpy.node import Node
import matplotlib.pyplot as plt
import json
import pathlib

class PlotJson(Node):

    def __init__(self):
        ''' 
        To Do :
        ------
        Find out how one can use positional arguments to define what the user want to plot
        Does this work or do we have to specify how often the node must run (only once here !)
        '''
        super().__init__('node')

        default_path = str(pathlib.Path(__file__).parent.absolute())
        default_path = default_path.replace('/build/realtime_statistics/realtime_statistics', '')

        self.driver_stats_path = default_path + "/ros2_realtime_statistics/data/driver_stats.json"
        self.controller_stats_path = default_path + "/ros2_realtime_statistics/data//controller_stats.json"

        json_data = self.read_json_file(self.driver_stats_path)
        self.plot_from_json(json_data)

    def read_json_file(self, path):
        with open(path, "r") as file:
            data = json.load(file)
        return data
    
    def plot_from_json(self, json_data):
        self.fig, self.axs = plt.subplots(figsize=(12, 8))
        # plot for each keys



def main(args=None):
    rclpy.init(args=args)

    plt_json = PlotJson()

    rclpy.spin(plt_json)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    plt_json.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
