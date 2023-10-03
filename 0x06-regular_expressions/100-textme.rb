#!/usr/bin/env ruby

# Script should output: [SENDER],[RECEIVER],and [FLAGS]
matches = ARGV[0].scan(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/).flatten

puts matches.join(',')
