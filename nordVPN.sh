#!/bin/bash

# Bash Script for using NordVPN servers as proxies for request.py

for k in pl al cr us gr lv ch pt ch ar hr hk lu ro tw au cy hu my rs th at cz is mx tr be dk md sk ua ba ee nl si uk br 'in' it fi ie nz za bg fr il mk kr vn ca ge no es cl de jp se sg
do
  for i in {0..2999}
	do
	nordvpn c $k$i && python3 request.py && number=$((number + 1))
	echo "success number: $number"
	done
echo "Done"
echo "success number: $number"
done
