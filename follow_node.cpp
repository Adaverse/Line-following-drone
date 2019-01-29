#include <ros/ros.h>
#include <mavros_msgs/OverrideRCIn.h>
#include <mavros_msgs/RCIn.h>
#include <std_msgs/Int32.h>
#define RC rc_ovrd.channels

mavros_msgs::OverrideRCIn rc_ovrd;
std_msgs::Int32 line_cmd;
mavros_msgs::RCIn over_switch;

int kill ;
int line_cmd ;

void rc_cb(const mavros_msgs::RCIn::ConstPtr& msg2){
    over_switch = *msg2;
    kill = over_switch.channels[5];
}

void line_cb(const std_msgs::Int32::ConstPtr& msg){
    line_cmd = *msg;
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "line_follower_node");
    ros::NodeHandle nh;
    ros::Subscriber rc_sub = nh.subscribe<mavros_msgs::RCIn>("mavros/rc/in", 10, rc_cb);
    ros::Subscriber line_sub = nh.subscribe<std_msgs::Int32>("line_dist", 10, line_cb);
    ros::Publisher radio_pub = nh.advertise<mavros_msgs::OverrideRCIn>("mavros/rc/override", 10);

    ros::Rate rate(60.0);

    while (ros::ok())
    {
        if(kill<1200)
        {
            RC[0] = 1500;
            RC[1] = 1400;
            RC[2] = 1500;
            RC[3] = 1500;
            RC[4] = 1100;
            RC[5] = 1000;
            RC[6] = 1100;
            RC[7] = 1100;
            
            if(line_cmd == 1){
            	RC[0] = 1650; // move rightwards
            	ROS_INFO("Moving Rightwards");
            }else if (line_cmd == -1){ 
            	RC[0] = 1350; // move leftwards
            	ROS_INFO("Moving Leftwards");
            }
            
            radio_pub.publish(rc_ovrd);
            ros::spinOnce();
            rate.sleep();
        }
    }

    return 0;
}
