#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int64.hpp"

using namespace std;

class CNumberCounterNode : public rclcpp::Node
{
public:
    CNumberCounterNode() : Node("number_counter")
    {
        m_subscriber = this->create_subscription<std_msgs::msg::Int64>("number", 10, std::bind(&CNumberCounterNode::number_callback, 
            this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "number counter node created successfully!");
    }

private:
    rclcpp::Subscription<std_msgs::msg::Int64>::SharedPtr m_subscriber;
    rclcpp::Publisher<std_msgs::msg::Int64>::SharedPtr m_publisher;

    void number_callback(const std_msgs::msg::Int64::SharedPtr msg) const
    {
        RCLCPP_INFO(this->get_logger(),  "Number received: %ld", msg->data);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<CNumberCounterNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}