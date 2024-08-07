import io
import sys, os
import time
from io import StringIO
from unittest import mock


def mockAndRun(input_lines: list, method):
    new_stdin = io.TextIOWrapper(
        io.BytesIO("\n".join(input_lines).encode("utf-8")), encoding="utf-8"
    )
    with mock.patch("sys.stdin", new=new_stdin):
        old_stdout = sys.stdout
        sys.stdout = capturedStdOut = StringIO()
        method()
        sys.stdout = old_stdout
        value = capturedStdOut.getvalue()
        return value


def file_test(i, m):
    if not os.path.exists("input.txt"):
        open("input.txt", "x", encoding="utf-8").close()
    input_file = open("input.txt", "w", encoding="utf-8")
    try:
        input_file.write(i)
    finally:
        input_file.close()
    if not os.path.exists("output.txt"):
        open("output.txt", "x", encoding="utf-8").close()
    output_file = open("output.txt", "r", encoding="utf-8")
    try:
        m()
        result = output_file.read()
    finally:
        output_file.close()
    return result


def time_file_test(i, m):
    if not os.path.exists("input.txt"):
        open("input.txt", "x", encoding="utf-8").close()
    input_file = open("input.txt", "w", encoding="utf-8")
    try:
        input_file.write(i)
    finally:
        input_file.close()
    if not os.path.exists("output.txt"):
        open("output.txt", "x", encoding="utf-8").close()
    output_file = open("output.txt", "r", encoding="utf-8")
    try:
        start_time = time.perf_counter()
        print(start_time)
        m()
        result_time = time.perf_counter() - start_time
        print(time.perf_counter())
        result = output_file.read()
        print(time.perf_counter())
    finally:
        output_file.close()
    return result, result_time
