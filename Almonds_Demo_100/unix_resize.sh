#!/bin/sh


if [ $1 == true ]
then
	printf '\e[8;25;80t'
fi

if [ $1 == false ]
then
	printf '\e[8;32;100t'
fi
