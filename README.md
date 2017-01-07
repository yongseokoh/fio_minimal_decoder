FIO Minimal Decoder
===================

FIO (https://github.com/axboe/fio) minimal output decoder written in Python

Example 
=======

    #fio --name=test --filename=/dev/nvme0n1  --ioengine=libaio --iodepth=128 --bs=4k --rw=randread --runtime=60 --minimal --output=minimal.output

    #./fio_minimal_output_decode.py minimal.output
    
    Input Minimal File =  minimal.output
    0	terse_version	fio: terminating on signal 2
    3
    1	fio_version	fio-2.11-4-g34feb
    2	jobname	test
    3	groupid	0
    4	error	0
    5	read_kb	99468
    6	read_bandwidth	53912
    7	read_iops	13478
    8	read_runtime	1845
    9	read_slat_min	38
    10	read_slat_max	223
    11	read_slat_mean	71.418024
    12	read_slat_dev	22.554483
    13	read_clat_max	9
    14	read_clat_min	10559
    15	read_clat_mean	9387.169059
    16	read_clat_dev	564.646711
    17	read_clat_pct01	1.000000%=6944
    18	read_clat_pct02	5.000000%=9280
    19	read_clat_pct03	10.000000%=9280
    20	read_clat_pct04	20.000000%=9408
    21	read_clat_pct05	30.000000%=9408
    22	read_clat_pct06	40.000000%=9408
    23	read_clat_pct07	50.000000%=9408
    ...
    110	lat_4ms	0.11%
    111	lat_10ms	98.77%
    112	lat_20ms	1.01%
    113	lat_50ms	0.00%
    114	lat_100ms	0.00%
    115	lat_250ms	0.00%
    116	lat_500ms	0.00%
    117	lat_750ms	0.00%
    118	lat_1000ms	0.00%
    119	lat_2000ms	0.00%
    120	lat_over_2000ms	0.00%
    121	disk_name	nvme0n1
    122	disk_read_iops	23605
    123	disk_write_iops	0
    124	disk_read_merges	0
    125	disk_write_merges	0
    126	disk_read_ticks	1312
    127	write_ticks	0
    128	disk_queue_time	1304
