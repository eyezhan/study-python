#!/bin/bash

usage()
{
    echo "usage: ./execute.sh [test plan]"
    echo "Default test plan is 'test.plan'."
}

if [ $# -gt 1 ]; then
    usage
    exit -1
fi

export CASE_DIR=/c/workspace/ai-auto-test/cases

if [ -z $1 ]; then
    test_plan='test.plan'
else
    test_plan=$1
fi

log=`echo $test_plan | awk -F'.' '{print $1}'`.log
> $log
for i in `cat test.plan`; do
    i=`echo $i | tr -d '\r'`
    echo "================================="
    echo Test Case: $i
    $CASE_DIR/$i $i
    retval=$?
    if [ $retval -eq 0 ]; then
        test_res=`grep 'Test Result' $i/$i.log | tail -1 | awk '{print $NF}'`
        comments=`grep 'Comments' $i/$i.log | tail -1 | awk -F'Comments: ' '{print $NF}'`
    else
        test_res='FAIL'
        comments='Fail to run test case.'
    fi
    echo "$i|$test_res|$comments" >> $log
done
