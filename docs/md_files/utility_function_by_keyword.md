<!--
 *  Created Date: Friday, February 16th 2024
 *  Contact Info: luoxiangyong01@gmail.com
 *  Author/Copyright: Mr. Xiangyong Luo
-->

## Message From pyufunc Developers

This document is designed to serve as an invaluable resource for developers, offering an extensive list of existing utility functions organized by keywords. The use of keywords for organization purposes aims to streamline the search process, enabling developers to quickly and efficiently find the specific functions they need to enhance their projects. Utility functions play a crucial role in software development, providing pre-built solutions to common problems and tasks, thereby saving time and reducing the complexity of coding from scratch. By presenting these functions in a keyword-centric format, we facilitate a more intuitive and user-friendly approach to accessing a vast repository of tools, ensuring that developers can leverage the full potential of utility functions to optimize their code, improve performance, and innovate within their applications.

This methodical approach empowers developers to efficiently identify the functions that best match their current requirements, thereby enhancing their coding workflow and productivity. Whether tackling complex algorithmic challenges or implementing basic functionality, this guide aims to be an essential companion, fostering a deeper understanding and more effective use of utility functions in software development projects.

## Existing Utility Functions by Keywords

Available utility functions in pyufunc:

Note: we may not update available functions in time, please run code below to check latest available functions.

```python
pyufunc.show_util_func_by_keyword()
```

Available utility functions in pyUFunc (152):

- non-keywords:
  - add_date_in_filename
  - add_dir_to_env
  - add_pkg_to_sys_path
  - count_lines_of_code
  - dataclass_dict_wrapper
  - dict_delete_keys
  - dict_split_by_chunk
  - download_elevation_tif_by
  - end_of_life
  - extend_dataclass
  - func_running_time
  - func_time
  - import_package
  - log_logger
  - log_writer
  - merge_dataclass
  - path2linux
  - path2uniform
  - pickle_load
  - pickle_save
  - printer_file
  - r2_score
  - remove_duplicate_files
  - remove_file
  - requires
  - send_email
  - str_strip
  - timeout
  - timeout_linux
  - with_argparse

- show:
  - show_dir_in_tree
  - show_docstring_google
  - show_docstring_headers
  - show_docstring_numpy
  - show_util_func_by_category
  - show_util_func_by_keyword

- get:
  - get_coordinates_from_geom
  - get_dir_size
  - get_file_size
  - get_filenames_by_ext
  - get_files_by_ext
  - get_host_ip
  - get_host_name
  - get_layer_boundary
  - get_osm_place
  - get_terminal_height
  - get_terminal_width
  - get_time_diff_in_unit
  - get_timezone
  - get_user_defined_func
  - get_user_defined_module
  - get_user_imported_module

- generate:
  - generate_dir_with_date
  - generate_password
  - generate_unique_filename

- create:
  - create_circle_at_point_with_radius
  - create_dataclass
  - create_dataclass_from_dict
  - create_tempfile
  - create_unique_filename

- find:
  - find_closest_point
  - find_duplicate_files
  - find_executable_from_PATH_on_win
  - find_fn_from_PATH_on_win
  - find_k_nearest_points
  - find_util_func_by_keyword

- calc:
  - calc_area_from_wkt_geometry
  - calc_distance_on_unit_haversine
  - calc_distance_on_unit_sphere

- run:
  - run_parallel

- group:
  - group_dt_daily
  - group_dt_hourly
  - group_dt_minutely
  - group_dt_monthly
  - group_dt_weekly
  - group_dt_yearly

- check:
  - check_file_existence
  - check_filename
  - check_files_in_dir
  - check_platform

- validate:
  - validate_url

- list:
  - list_all_timezones
  - list_flatten_nested
  - list_split_by_equal_sublist
  - list_split_by_fixed_length

- img:
  - img_bytes_to_CV
  - img_bytes_to_PIL
  - img_CV_to_bytes
  - img_CV_to_PIL
  - img_PIL_to_bytes
  - img_PIL_to_CV
  - img_resize
  - img_rotate
  - img_rotate_bound
  - img_show
  - img_to_bytes
  - img_translate

- fmt:
  - fmt_dt_to_str
  - fmt_str_to_dt

- cvt:
  - cvt_baidu09_to_gcj02
  - cvt_baidu09_to_wgs84
  - cvt_current_dt_to_tz
  - cvt_digit_str_to_float
  - cvt_digit_str_to_int
  - cvt_gcj02_to_baidu09
  - cvt_gcj02_to_wgs84
  - cvt_int_to_alpha
  - cvt_wgs84_to_baidu09
  - cvt_wgs84_to_gcj02

- is:
  - is_CV_img
  - is_float
  - is_linux
  - is_mac
  - is_module_importable
  - is_PIL_img
  - is_user_defined_func
  - is_valid_email
  - is_windows

- proj:
  - proj_point_to_line

- github:
  - github_file_downloader
  - github_get_status

- pypi:
  - pypi_downloads

- error:
  - mean_absolute_error
  - mean_absolute_percentage_error
  - mean_percentage_error
  - mean_squared_error
  - mean_squared_log_error
  - root_mean_squared_error

- algo:
  - algo_bubble_sort
  - algo_heap_sort
  - algo_insertion_sort
  - algo_merge_sort
  - algo_quick_sort
  - algo_selection_sort

- gmns:
  - gmns_geo
  - gmns_read_link
  - gmns_read_node
  - gmns_read_poi
  - gmns_read_zone
  - GMNSAgent
  - GMNSLink
  - GMNSNode
  - GMNSPOI
  - GMNSZone

- pytest:
  - pytest_show_assert
  - pytest_show_database
  - pytest_show_fixture
  - pytest_show_naming_convention
  - pytest_show_parametrize
  - pytest_show_raise
  - pytest_show_skip_xfail
  - pytest_show_warning
