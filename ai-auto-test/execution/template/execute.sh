#!/bin/bash

usage()
{
cat << EOF
This script execute test case(s) list in test plan file.
Return value: 0        OK
              Other    Error

OPTIONS:
    -h    Show help message.
    -p    Test plan. Default: test.plan
EOF
}

while getopts "hp:" OPTION
do
    case $OPTION in
        h)
            usage
            exit 1
            ;;
        p)
            test_plan=$OPTARG
            ;;
     esac
done

# Update repo to latest version.
git pull

# Set default test plan.
if [ -z $test_plan ]; then
    test_plan=test.plan
fi
echo Test Plan: $test_plan

CASE_DIR=../../cases

log_path=logs/`date +'%Y%m%d_%H%M%S'`
if [ ! -d $log_path ]; then
    mkdir -p $log_path
fi
echo Log Path: $log_path
log=`echo $test_plan | awk -F'.' '{print $1}'`.log
> $log

# Execute test cases listed in test plan.
for i in `cat test.plan`; do
    i=`echo $i | tr -d '\r'`
    echo "================================="
    echo Test Case: $i
    $CASE_DIR/$i $log_path/$i
    retval=$?
    if [ $retval -eq 0 ]; then
        test_res=`grep 'Test Result' $log_path/$i/$i.log | tail -1 | awk '{print $NF}'`
        comments=`grep 'Comments' $log_path/$i/$i.log | tail -1 | awk -F'Comments: ' '{print $NF}'`
    else
        test_res='FAIL'
        comments='Fail to run test case.'
    fi
    echo "$i|$test_res|$comments" >> $log
done

# Generate excel test report.
echo "================================="
if [ ! -d reports ]; then
    mkdir reports
fi
report_fn=reports/`basename $log_path`.xlsx
python gen_test_report.py -p $test_plan -r $log_path -o $report_fn
