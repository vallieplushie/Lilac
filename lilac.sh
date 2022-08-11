#!/bin/bash

print_usage() {
  printf "usage: lilac [-options] [path to file]\n\t-v | Verbose: Print debug info"
}

lilac(){
  verbose='false'

  while getopts 'v:' flag; do
    case "${flag}" in
      v) verbose='true' ;;
      *) print_usage ;;
    esac
  done
}
