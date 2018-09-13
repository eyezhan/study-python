#!/usr/bin/env python
# coding=utf-8


import argparse
import json
import logging
import logging.config
import os
import re
import sys
import xlsxwriter


def gen_report(test_plan, results_dir, report_fn):
    # Create new work book.
    logger.info("Save report to: %s" % report_fn)
    wb = xlsxwriter.Workbook(report_fn)

    # Create formats.
    fmt = dict(
        font_name='Arial',
        font_size=10,
        align='center',
        border=1,
        bold=0)

    header_fmt = fmt.copy()
    header_fmt['bg_color'] = '#C00000'
    header_fmt['font_color'] = '#FFFFFF'
    header_fmt['bold'] = 1

    # Summary sheet formats.
    summary_header_fmt = wb.add_format(header_fmt)
    summary_num_fmt = wb.add_format(fmt)

    # Percent data format.
    fmt['num_format'] = '0.00%'
    percent_fmt = wb.add_format(fmt)
    fmt.pop('num_format')

    # Result sheet formats.
    header_fmt['align'] = 'left'
    fmt['align'] = 'left'
    result_header_fmt = wb.add_format(header_fmt)
    result_fmt = wb.add_format(fmt)

    # # Pass/Fail results formats.
    # pass_fmt = wb.add_format(
    #     {'bg_color': '#C6EFCE', 'font_color': '#006100', 'border': 1})
    # fail_fmt = wb.add_format(
    #     {'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'border': 1})
    # na_fmt = wb.add_format(
    #     {'bg_color': '#FFEB9C', 'font_color': '#9C8000', 'border': 1})

    # Create table in summary sheet
    summary_ws = wb.add_worksheet('Summary')

    headings = ['Pass', 'Fail', 'N/A', 'Total', 'Pass Rate']
    summary_ws.set_column('%s:%s' % (chr(65), chr(len(headings) + 65)), 20)
    for i in range(len(headings)):
        summary_ws.write_string(0, i, headings[i], summary_header_fmt)

    # Get case list.
    case_lst = [line.strip() for line in open(test_plan, 'r')]

    # Add sheet for test result.
    sheet_name = os.path.basename(results_dir)
    ws = wb.add_worksheet(sheet_name)

    # Create table header.
    headings = ['Case Name', 'Test Result', 'Comments']
    for i in range(len(headings)):
        ws.write_string(0, i, headings[i], result_header_fmt)
    ws.set_column('A:A', 60)
    ws.set_column('B:B', 15)
    ws.set_column('C:C', 50)

    # row = 1
    data_lst = [case_lst]
    res_lst = list()
    comments_lst = list()
    for test_case in case_lst:
        case_log = os.path.join(results_dir, test_case, test_case + '.log')
        comments = ''
        if os.path.exists(case_log):
            # Get test result.
            f = re.compile('Test Result: (.*)').findall(open(case_log).read())
            if f:
                test_res = f[-1]
            else:
                test_res = 'FAIL'

            # Get comments.
            f = re.compile('Comments: (.*)').findall(open(case_log).read())
            if f:
                comments = f[-1]
            else:
                if test_res == 'FAIL':
                    comments = 'Fail to run test case.'
        else:
            test_res = 'FAIL'
            comments = 'Fail to run test case.'
        test_res = test_res.strip().lower()
        res_lst.append(test_res)
        comments_lst.append(comments)
        # if test_res == 'pass':
        #     tmp_fmt = pass_fmt
        # elif test_res == 'fail':
        #     tmp_fmt = fail_fmt
        # else:
        #     tmp_fmt = na_fmt
        # ws.write_string(row, 0, test_case, tmp_fmt)
        # ws.write_string(row, 1, test_res, tmp_fmt)
        # ws.write_string(row, 2, comments, tmp_fmt)
        # row += 1
    data_lst.append(res_lst)
    data_lst.append(comments_lst)
    ws.write_column(1, 0, data_lst[0], result_fmt)
    ws.write_column(1, 1, data_lst[1], result_fmt)
    ws.write_column(1, 2, data_lst[2], result_fmt)

    summary_ws.write_formula(1, 0, "=_xlfn.COUNTIF('%s'!B2:B%d, \"pass\")" %
                             (sheet_name, len(case_lst) + 1), summary_num_fmt)
    summary_ws.write_formula(1, 1, "=_xlfn.COUNTIF('%s'!B2:B%d, \"fail\")" %
                             (sheet_name, len(case_lst) + 1), summary_num_fmt)
    summary_ws.write_formula(1, 2, '=%s2-%s2-%s2' %
                             (chr(3 + 65), chr(0 + 65), chr(1 + 65)), summary_num_fmt)
    summary_ws.write_number(1, 3, len(case_lst), summary_num_fmt)
    summary_ws.write_formula(1, 4, '=%s2/%s2' %
                             (chr(0 + 65), chr(3 + 65)), percent_fmt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate test report.')
    parser.add_argument(
        '-p',
        '--test_plan',
        default='test.plan',
        help='Test plan.')
    parser.add_argument(
        '-r',
        '--results_dir',
        required=True,
        help='Test result dir.')
    parser.add_argument(
        '-o',
        '--report',
        default='TestReport.xls',
        help='Test report.')

    args = parser.parse_args()

    cmd = 'ln %s logging.json' % os.path.join(
        os.getcwd(), os.pardir, os.pardir, 'cases', 'logging.json')
    os.popen(cmd)

    results_dir = args.results_dir
    log_fn = os.path.join(
        results_dir, '%s.log' %
        os.path.basename(results_dir))
    conf_data = json.load(open('logging.json', 'r'))
    conf_data['handlers']['file_handler']['filename'] = log_fn
    try:
        logging.config.dictConfig(conf_data)
    except Exception as e:
        sys.exit(e)
    logger = logging.getLogger()

    logger.info(' '.join(sys.argv))
    logger.info("Generating test report...")
    test_plan = os.path.abspath(args.test_plan)
    if not os.path.exists(test_plan):
        logging.error('Fail to found test plan %s' % test_plan)
        sys.exit(-1)

    logger.info(os.listdir(args.results_dir))
    if len(os.listdir(args.results_dir)) < 2:
        logging.error('No test result in directory %s' % args.results_dir)
        sys.exit(-1)

    report_fn = os.path.abspath(args.report)
    if not os.path.exists(os.path.dirname(report_fn)):
        os.makedirs(os.path.dirname(report_fn))

    gen_report(test_plan, results_dir, report_fn)
