import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

# Example of logging in a data pipeline. This is a simple demonstration of how to use logging to track the progress and errors in a data pipeline. 
# In a real-world scenario, you would replace the example code with actual data processing steps.
logging.debug("Pipeline Started")
logging.info("Pipeline Started")
logging.warning("Pipeline Started")
logging.error("Pipeline Started")
logging.critical("Pipeline Started")

try:
    amount = "100"
    total = amount + 50
    logging.info(f"Total amount calculated: {total}")
except Exception as e:
    logging.error(f"Pipeline Failed: {e}")

logging.info("Pipeline Completed")
# 2026-04-12 18:29:58 - INFO - Pipeline Started
# 2026-04-12 18:29:58 - ERROR - Pipeline Failed: can only concatenate str (not "int") to str
# 2026-04-12 18:29:58 - INFO - Pipeline Completed