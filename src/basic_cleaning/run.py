#!/usr/bin/env python
"""
<<<<<<< HEAD
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
=======
Performs the cleaning of the data and save it in the wandb.
>>>>>>> 890a5e60a4f272fe070836685b2d63a04a62f2fd
"""
import argparse
import logging
import wandb
<<<<<<< HEAD
import pandas as pd
import os
=======
>>>>>>> 890a5e60a4f272fe070836685b2d63a04a62f2fd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)
<<<<<<< HEAD
    
    logger.info('Downloading/Reading artifact')
    artifact_path = run.use_artifact(args.input_artifact).file()
    df = pd.read_csv(artifact_path)
    
    logger.info('Removing Outliers')
    idx = df.price.between(args.min_price, args.max_price)
    df = df[idx].copy()
    
    logger.info('Converting last_review to datetime')
    df['last_review'] = pd.to_datetime(df.last_review)
    
    logger.info('Dropping improper rows in the dataset')
    idx = df.longitude.between(-74.25, 73.50) & df.latitude.between(40.5, 41.2)
    df = df[idx].copy()
    
    logger.info('Saving the cleaned data')
    file_name = 'clean_sample.csv'
    df.to_csv(file_name, index=False)
    
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(file_name)
    
    logger.info('Logging artifact')
    run.log_artifact(artifact)
    
    os.remove(file_name)
    
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help='Raw data',
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help='Cleaned data',
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help='Type of the artifact',
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help='Description for the artifact',
=======

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This cleans the data.")


    parser.add_argument(
        "--parameter1", 
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
>>>>>>> 890a5e60a4f272fe070836685b2d63a04a62f2fd
        required=True
    )

    parser.add_argument(
<<<<<<< HEAD
        "--min_price", 
        type=float,
        help="Minimum price for cleaning outliers",
=======
        "--parameter2", 
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
>>>>>>> 890a5e60a4f272fe070836685b2d63a04a62f2fd
        required=True
    )

    parser.add_argument(
<<<<<<< HEAD
        "--max_price", 
        type=float,
        help="Maximum price for cleaning outliers",
=======
        "--parameter3", 
        type=## INSERT TYPE HERE: str, float or int,
        help=## INSERT DESCRIPTION HERE,
>>>>>>> 890a5e60a4f272fe070836685b2d63a04a62f2fd
        required=True
    )


    args = parser.parse_args()

    go(args)
