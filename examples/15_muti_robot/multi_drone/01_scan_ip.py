# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from multi_robomaster import multi_robot


if __name__ == '__main__':
    multi_drone = multi_robot.MultiDrone()
    drone_ip_list = multi_drone._scan_multi_robot(2)
    print("scan ip result: {0}".format(drone_ip_list))


