import json
import logging
import os.path
import string
import csv
from zipfile import ZipFile

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation


def extract_text_from_pdf(pdf_file_name: str):

    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    try:
        # get base path.
        # base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        base_path= os.path.dirname(os.path.abspath(__file__))
        # print(base_path)
        # Initial setup, create credentials instance.
        credentials = Credentials.service_account_credentials_builder() \
            .from_file(base_path + "/pdfservices-api-credentials.json") \
            .build()

        # Create an ExecutionContext using credentials and create a new operation instance.
        execution_context = ExecutionContext.create(credentials)
        extract_pdf_operation = ExtractPDFOperation.create_new()

        # Set operation input from a source file.
        source = FileRef.create_from_local_file(base_path + "/resources/{}".format(pdf_file_name))
        extract_pdf_operation.set_input(source)

        # Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_element_to_extract(ExtractElementType.TEXT) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

        # Execute the operation.
        result: FileRef = extract_pdf_operation.execute(execution_context)

        # Save the result to the specified location.
        result.save_as(base_path + "/output/ExtractTextInfoFromPDF.zip")

        with ZipFile(base_path + '/output/ExtractTextInfoFromPDF.zip', 'r') as zip:
            zip.extractall()
            zip.close()
        
        return json.load(open(base_path + '/structuredData.json', 'r', encoding="utf8"))

    except (ServiceApiException, ServiceUsageException, SdkException):
        logging.exception("Exception encountered while executing operation")

    


print(extract_text_from_pdf("extractPdfInput.pdf"))



def read_csv_team_skill (csv_file_name: str):
    teams = {}

    with open(csv_file_name, newline='') as grossFile:
        spamreader = csv.reader(grossFile, delimiter=',', quotechar='|')
        next(smapreader)
        for row in spamreader:
            teams[row[0]] = row[1]

    grossFile.close()

    teams_skillset = {}

    for key in teams:
        teams_skillset[key] = teams[key].split(";")

    return teams_skillset
