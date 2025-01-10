from launch import LaunchDescription    
from launch.actions import RegisterEventHandler, LogInfo
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node



def generate_launch_description():
    
    spawn_joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '-c', '/controller_manager'],
        output='screen',
    )
    
    spawn_robot_velocity_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['mowbot_velocity_controller', '-c', '/controller_manager'],
        output='screen',
    )
    
    diffdrive_controller_spawn_callback = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=spawn_joint_state_broadcaster,
            on_exit=[spawn_robot_velocity_controller],
        )
    )
    
    return LaunchDescription([
        spawn_joint_state_broadcaster,
        diffdrive_controller_spawn_callback,
    ])