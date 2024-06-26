#!/usr/bin/env python
import os
import csv

def csv_to_line_proto(csvText, tagsDict, measNames):
    fmtString = 'collector'
    if tagsDict:
        fmtString += ',' + _get_tag_string(tagsDict)

    fmtString += ' '
    fmtString += _get_value_format_string_for_meas(measNames)

    reader = csv.reader(csvText.splitlines(), quoting=csv.QUOTE_NONNUMERIC)
    rows = []
    for row in reader:
        timestamp = row.pop()
        rows.append(fmtString.format(*row) + ' {:d}'.format(int(timestamp)))
    return '\n'.join(rows)

def _get_tag_string(tagsDict):
    tagList = []
    for key, value in tagsDict.items():
        tagList.append('{}={}'.format(key, value))
    return ','.join(tagList)

def _get_value_format_string_for_meas(measNames):
    valueList = []
    for measName in measNames:
        valueList.append('{}={{}}'.format(measName))
    return ','.join(valueList)
