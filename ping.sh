#!/bin/bash
p1=$1
p2=$2

if [ $p2 == "router" ]
then
  if [ $p1 == "node1" ]
  then
    sudo ip netns exec node1 ping 172.0.0.1
  elif [ $p1 == "node2" ]
  then
    sudo ip netns exec node2 ping 172.0.0.1
  elif [ $p1 == "node3" ]
  then
    sudo ip netns exec node3 ping 10.10.0.1
  else
    sudo ip netns exec node4 ping 10.10.0.1
  fi
elif [ $p2 == "node1" ]
then
  sudo ip netns exec $p1 ping 172.0.0.2
elif [ $p2 == "node2" ]
then
  sudo ip netns exec $p1 ping 172.0.0.3
elif [ $p2 == "node3" ]
then
  sudo ip netns exec $p1 ping 10.10.0.2
else
  sudo ip netns exec $p1 ping 10.10.0.3
fi