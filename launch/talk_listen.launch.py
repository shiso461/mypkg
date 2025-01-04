# SPDX-FileCopyrightText: 2025 Soma Shirai <shiso461@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    iss_position  = launch_ros.actions.Node(
        package='mypkg',
        executable='iss_position',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([iss_position, listener])
