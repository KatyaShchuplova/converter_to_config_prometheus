# converter_to_config_prometheus
in prometheus.yml:

  - job_name: 'dummy'
    file_sd_configs:
      - files:
        - targets.yml


script options (youneed to edit script):
SOURCE_FILE = "path_to_ansible_inventory"
OUT_FILE = "targets.yml"

