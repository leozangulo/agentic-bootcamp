# IBM Watsonx Orchestrate AskBenefits Agent - Setup Guide

This guide walks you through the complete process of creating, configuring, and deploying agents within IBM Watsonx Orchestrate (WxO). By following this step-by-step guide with visual instructions, you'll learn how to build an AI-powered healthcare assistant capable of accurately responding to benefits-related inquiries.

## Table of Contents
- [Lab Overview](#lab-overview)
- [Agents Overview](#agents-overview)
- [Lab Objective](#lab-objective)
- [Use Case Description](#use-case-description)
- [Architecture Diagram](#architecture-diagram)
- [Prerequisites](#prerequisites)
- [AskBenefits Step-by-Step Instructions](#askbenefits-step-by-step-instructions)
  - [1. Accessing IBM Watsonx Orchestrate](#1-accessing-ibm-watsonx-orchestrate)
  - [2. Creating a New Agent](#2-creating-a-new-agent)
  - [3. Importing and Attaching Tools](#3-importing-and-attaching-tools)
  - [4. Deploying and Testing the Agent](#4-deploying-and-testing-the-agent)
- [AskDental Step-by-Step Instructions](#askdental-step-by-step-instructions)
  - [1. Identifying Knowledge Gaps](#1-identifying-knowledge-gaps)
  - [2. Creating a New Collaborator Agent](#2-creating-a-new-collaborator-agent)
  - [3. Importing and Exposing Knowledge Documents](#3-importing-and-exposing-knowledge-documents)
  - [4. Integrating AskDental as a Collaborator](#4-integrating-askdental-as-a-collaborator)
- [Testing Scenarios](#testing-scenarios)
- [Incorporating a WatsonX Assistant (Optional)](#incorporating-a-watsonx-assistant)
  - [1. Creating a new WatsonX Assistant](#1-creating-a-new-watsonx-assistant)
  - [2. Importing the Pre-Made Action](#2-importing-the-pre-made-action)
  - [3. Publishing the Assistant](#3-publishing-the-assistant)
  - [4. Getting Assistant Variables](#4-getting-assistant-variables)
  - [5. Generating an API Key](#5-generating-an-api-key)
  - [6. Importing the Assistant](#6-importing-the-assistant)
- [Secondary Testing Scenarios](#secondary-testing-scenarios)
- [AskReporting Step-by-Step Instructions (Optional)](#askreporting-step-by-step-instructions)
  - [1. Create AskReporting](#1-create-askreporting)
  - [3. Importing and Attaching Tools](#2-importing-and-attaching-tools)
  - [3. Switching to and Testing the Agent](#3-switching-to-and-testing-the-agent)
- [Final Testing Scenarios](#final-testing-scenarios)

---

## Use Case Description

This use case focuses on developing and deploying an AskBenefits agent using IBM watsonx Orchestrate, as illustrated in the accompanying architecture. The agent enables users to interact with healthcare systems through conversational AI to access personalized benefits information. In this lab, you will build the AskBenefits agent from scratch, integrating external tools via OpenAPI to retrieve medical history, identify overdue care, and provide upcoming procedure guidance. You'll also create a companion AskDental agent that references uploaded documents to answer dental coverage questions, and configure both agents to collaborate, showcasing a multi-agent orchestration pattern for comprehensive healthcare support.

---

## Architecture Diagram

  ![Architecture Diagram](assets/askbenefits_architecture.png)

---

## Prerequisites

* An active IBM Cloud account
* Access to IBM Watsonx Orchestrate environment
* The OpenAPI specification file (`openapi-tools-spec.json`)
* The benefits file (`dental_benefits_summary.pdf`)
* The optional WatsonX Assistant action file (`main-desk-concierge-action-v1.json`)
* The optional reporting OpenAPI specification file  (`openapi-tools-report.json`)

---

## AskBenefits Step-by-Step Instructions

### 1. Accessing IBM Watsonx Orchestrate

1. Navigate to [https://cloud.ibm.com/](https://cloud.ibm.com/)

   ![IBM Cloud Homepage](assets/1_ibm_cloud.png)

2. Click on the menu icon in the top left corner

   ![Click menu icon](assets/2_hamburger.png)

3. Select "Watson Orchestrate-itz"

   ![Select Watson Orchestrate](assets/3_resource_list.png)

4. Click "Launch watsonx Orchestrate"

   ![Launch Watsonx Orchestrate](assets/4_launch_wxo.png)

5. Click on the hamburger menu icon in the top left

   ![Click hamburger menu](assets/5_hamburger.png)

6. Click on "Build"

   ![Click Build option](assets/6_build.png)

7. Select "Agent Builder"

   ![Select Agent Builder](assets/7_agent_builder.png)

### 2. Creating a New Agent

1. Click "Create agent"

   ![Click Create agent](assets/8_create_agent.png)

2. In the "Name*" field, enter:
   ```
   AskBenefits
   ```

   ![Enter agent name](assets/9_paste_name.png)

3. In the "Description*" field, enter:
   ```
   A proactive healthcare assistant designed to guide users through questions related to medical procedures and health plan benefits. The agent classifies each inquiry as pertaining to a past, future, or overdue medical procedure and selects the most appropriate tool accordingly. It can retrieve historical data, identify overdue care, offer guidance on upcoming procedures, or provide plan-specific details such as coverage and pharmacy benefits. When necessary, it can also assist in scheduling appointments. The assistant reasons step-by-step, selects tools based strictly on user intent, avoids redundant calls, and responds with professionalism, clarity, and empathy.
   ```

   ![Enter agent description](assets/10_paste_description.png)

4. Click "Create" to initialize your agent

   ![Click Create button](assets/11_create_agent.png)

### 3. Importing and Attaching Tools

1. Click "Add tool"

   ![Click Add tool](assets/14_add_tool.png)

2. Select "Import an external tool."

   ![Select Import](assets/15_import_tool.png)

3. Click on the upload area labeled "Drag and drop OpenAPI files here or click to upload."

   ![Click upload area](assets/16_upload_spec.png)

4. Upload the file containing the OpenAPI specification file: `openapi-tools-spec.json`  (Note: `openapi-tools-spec.yaml` is also available if issues are encountered with file uploads)

5. Click "Next"

   ![Click Next](assets/17_click_next.png)

6. Click "Select all rows in the table" to select all available tools

   ![Select all rows](assets/18_select_tools.png)

7. Click "Done"

   ![Click Done](assets/19_finalize_tool.png)

### 4. Deploying and Testing the Agent

1. In the "Type something..." field enter the following and hit enter
   ```
   Can you give me a cost breakdown for X rays?
   ```

   ![Test Agent](assets/20_test_agent.png)


2. Click "Deploy" to activate your AskBenefits agent

   ![Test Agent](assets/21_deploy.png)

3. Click on the menu icon in the top left corner

   ![Navigate to Menu](assets/22_hamburger.png)

4. Click on "Chat" 

   ![Navigate to Chat](assets/23_chat.png)

---

## AskDental Step-by-Step Instructions

### 1. Identifying Knowledge Gaps

1. In the "Type something..." field enter the following and hit enter
   ```
   Can you describe my dental benefits?
   ```

   ![Test Agent](assets/24_start_chat.png)

### 2. Creating a New Collaborator Agent

1. Click on the hamburger menu icon in the top left

   ![Click hamburger menu](assets/25_hamburger.png)

2. Click on "Build"

   ![Click Build option](assets/26_build.png)

3. Select "Agent Builder"

   ![Select Agent Builder](assets/27_agent_builder.png)

4. Click "Create agent"

   ![Click Create agent](assets/28_create_agent.png)

5. In the "Name*" field, enter:
   ```
   AskDental
   ```

   ![Enter agent name](assets/29_paste_name.png)

6. In the "Description*" field, enter:
   ```
   The dental benefits agent is a specialized AI assistant designed to provide personalized guidance and support to policyholders, helping them navigate their dental coverage and make informed decisions about their oral health care. By analyzing individual policy details and dental needs, the agent answers questions about coverage.
   ```

   ![Enter agent description](assets/30_paste_description.png)

7. Click "Create" to initialize your agent

   ![Click Create button](assets/31_create_agent.png)

### 3. Importing and Exposing Knowledge Documents

1. Click "Upload files" under "Knowledge

   ![Add New Files](assets/32_upload_files.png)

2. Upload the file containing Dental Benefit information: `dental_benefits_summary.pdf`

   ![Add Dental Benefits File](assets/33_upload_dental.png)

3. Click "Upload"

   ![Finalize Upload](assets/34_upload.png)

4. In the Knowledge Description field with "Example: This knowledge addresses all order-related inquiries. Customers can seek guidance on order status, shipping details, return policies, product availability, and refund processes." enter:
   ```
   This knowledge file explains dental benefits and can be used to answer questions to policyholders. Contains information about individual policy details and coverage. If the answer to the question is not contained in your knowledge base, instead of responding you should initiate a transfer to the supervisor agent, copying the users query verbatim.
   ```

   ![Click Add tool](assets/35_add_description.png)

5. Click "Deploy"

   ![Select Import](assets/36_deploy.png)

### 4. Integrating AskDental as a Collaborator

1. Click on the hamburger menu icon in the top left

   ![Click hamburger menu](assets/37_hamburger.png)

2. Click on "Build"

   ![Click Build option](assets/38_build.png)

3. Select "Agent Builder"

   ![Select Agent Builder](assets/39_agent_builder.png)

4. Select "AskBenefits"

   ![Select AskBenefits](assets/40_select_askbenefits.png)

5. Click "Add Agent" under "Agents"

   ![Add Collaborator Agent](assets/41_click_add_agent.png)

6. Select "Add from local instance"

   ![Add from Local Instance](assets/42_click_add_from_local_instance.png)

7. Select "AskDental"

   ![Select AskDental](assets/43_add_askdental.png)

8. Click "Add to agent"

   ![Add Collaborator to Agent](assets/44_add_to_agent.png)

9. Click "Deploy"

   ![Select Import](assets/45_deploy.png)

10. Click on the menu icon in the top left corner

   ![Navigate to Menu](assets/22_hamburger.png)

11. Click on "Chat" 

   ![Navigate to Chat](assets/23_chat.png)

12. In the "Type something..." field enter the following and hit enter
   ```
   Can you describe my dental benefits?
   ```

   ![Test Agent](assets/24_start_chat.png)

---

## Testing Scenarios

After successful deployment, test the AskBenefits agent with the following sample prompts to verify functionality across different healthcare scenarios:

1. **Procedure Cost Breakdown:**
   ```
   Can you give me a cost breakdown for X rays?
   ```

2. **Historical Procedure Review:**
   ```
   What procedures have we had at City Hospital in the last year?
   ```

3. **Preventive Care Alerts:**
   ```
   Are we overdue for any procedures?
   ```

4. **Appointment Scheduling:**
   ```
   Can you schedule an appointment for next Thursday at 10 AM?
   ```

5. **Document Access:**
   ```
   Thanks, how do I access my 1095 form again?
   ```

6. **Dental Document Question Answering:**
   ```
   Can you describe my dental benefits?
   ```


---

## Incorporating a WatsonX Assistant

### 1. Creating a new WatsonX Assistant

1. Click on the hamburger menu icon in the top left

   ![Click hamburger menu](assets/48_hamburger.png)
   ```

2. Click on "Build"

   ![Click Build option](assets/49_build.png)

3. Click on "Assistant Builder"

   ![Assistant Builder option](assets/50_assistant_builder.png)


4. In the "Assistant Name" field enter
   ```
   Main Desk Concierge
   ```
   ![Assistant Name](assets/51_assistant_name.png)

5. Click on "Next"

   ![Next](assets/52_next.png)

6. Select the "Web" option.

   ![Web Option](assets/53_web.png)

7. Select the "N/A (I am a student)" option.

   ![Student](assets/54_student.png)

8. Select the "Developer" option.

   ![Developer](assets/55_developer.png)

9. Select the "I’m using the product to complete a course or certification" option.

   ![Certification](assets/56_cert.png)

10. Click on "Next"

   ![Next](assets/57_next.png)

11. Type "Main Desk Concierge"

   ![Main Desk](assets/58_known_as.png)

12. Click on "Next"

   ![Next](assets/59_next.png)

13. Click "Create"

   ![Create](assets/60_create.png)

### 2. Importing the Pre-Made Action

1. Click "Actions"

   ![Actions](assets/61_actions.png)

2. Click on "Global Settings"

   ![Settings](assets/62_settings.png)

3. Click "Upload/Download"

   ![Upload/Download](assets/63_upload-download.png)

4. Click "Drag and drop file here or click to select a file" and upload `Main-Desk-Concierge-action.json`

   ![Upload File](assets/64_upload_file.png)

5. Click on "Upload"

   ![Upload](assets/65_upload.png)

6. Click "Upload and replace"

   ![Replace](assets/66_replace.png)

7. Click on "Close"

   ![Close](assets/67_close.png)

### 3. Publishing the Assistant

1. Click "Publish"

   ![Publish](assets/68_publish.png)

2. Click "Publish"

   ![Publish](assets/69_publish.png)

3. In the "Example: Updated "Business hours" action" field enter:
   ```
   First draft
   ```
   ![Description](assets/70_description.png)

4. Click "Choose environment"

   ![Environment](assets/71_choose_environment.png)

5. Click "Live"

   ![Live](assets/72_select_live.png)

6. Click "Publish"

   ![Publish](assets/73_publish.png)

### 4. Getting Assistant Variables

1. Click "Assistant settings"

   ![Assistant Settings](assets/74_assistant_settings.png)

2. Click "View details"

   ![View Details](assets/75_view_details.png)

3. Copy "Service Instance URL", "Assistant ID", "Live Environment ID" to a note on your machine

   ![Copy](assets/76_copy_1.png)

   ![Copy](assets/76_copy_2.png)

   ![Copy](assets/76_copy_3.png)

### 5. Generating an API Key

1. In a new tab, navigate to https://cloud.ibm.com/

2. Click "Manage"

   ![Manage](assets/77_manage.png)

3. Click "Access (IAM)"

   ![Access](assets/78_access.png)
   
4. Click "API keys"

   ![API Keys](assets/79_api.png)

5. Click "Create"

   ![Create](assets/80_create.png)

6. In "Name" field enter:
   ```
   wxo_key
   ```

7. Click "Create"

   ![Create](assets/81_create.png)

8. Copy API Key to Note on your local machine

   ![Create](assets/82_copy_to_local.png)

### 6. Importing the Assistant

1. Switch to tab WatsonX Orchestrate tab.

2. Click on the hamburger menu icon in the top left

   ![Click hamburger menu](assets/83_hamburger.png)

3. Click on "Build"

   ![Click Build option](assets/84_build.png)

4. Select "Agent Builder"

   ![Select Agent Builder](assets/85_agent_builder.png)

5. Select "AskBenefits"

   ![Select AskBenefits](assets/86_benefits.png)

6. Click "Add Agent" under "Agents"

   ![Add Collaborator Agent](assets/87_add_agent.png)

7. Click "Import and register an external agent."

   ![Import and Register](assets/88_import_agent.png)

8. Click "External watsonx Assistant"

   ![WxA Assistant](assets/89_external_wxa.png)

9. Click "Next"

   ![Next](assets/90_next.png)

10. Copy "API Key", "Environment ID", "Assistant ID", "Service Instance URL" into the respective fields from your local
   ![API](assets/91_api.png)

   ![Environment](assets/91_env.png)

   ![Assistant ID](assets/91_assistant_id.png)

   ![Service Instance URL](assets/91_url.png)

11. In the "Version" field enter:
   ```
   2024-08-25
   ```
   ![Version](assets/92_version.png)

12. In the "Display name" field enter:
   ```
   Main Desk
   ```
   ![Main Desk](assets/93_name.png)

13. In the "Description" field enter:
   ```
   This assistant collects necessary user information when they need to access their medical records
   ```
   ![Description](assets/94_description.png)

14. Click "Import agent"
   
   ![Import](assets/95_import_agent.png)

15. Click "Deploy"

   ![Deploy](assets/96_deploy.png)

---

## Secondary Testing Scenarios

After successful deployment, test the AskBenefits agent with the following sample prompts to verify functionality with the includeded Main Desk Assistant:

1. **Initiate Main Desk Assistant:**
   ```
   I need to access my medical history 
   ```

2. **Provide Name:**
   ```
   Charlie Smith
   ```

3. **Provide Date of Birth:**
   ```
   03-04-2013
   ```

4. **Previous Procedure Query:**
   ```
   When did I have my last vision exam?
   ```

5. **Follow-up on Previous Procedure Query:**
   ```
   and where was it?
   ```

---

## AskReporting Step-by-Step Instructions

### 1. Create AskReporting

1. Click on the hamburger menu icon in the top left

   ![Click hamburger menu](assets/97_hamburger.png)

2. Click on "Build"

   ![Click Build option](assets/98_build.png)

3. Select "Agent Builder"

   ![Select Agent Builder](assets/99_agent_builder.png)

4. Click "Create agent"

   ![Click Create agent](assets/100_create_agent.png)

5. In the "Name*" field, enter:
   ```
   AskReporting
   ```

   ![Enter agent name](assets/101_agent_name.png)

6. In the "Description*" field, enter:
   ```
   This agent is responsible for generating care reports that summarize the status and outcomes of healthcare claims. It reviews structured claim data and related correspondence to produce a clear, accessible summary of each claim’s history, current status, and resolution path. The generated reports highlight key financial details, adjustments, patient responsibility, and any reprocessing actions (e.g., appeals, denials, or approvals). These reports are optimized for use by providers, payers, and care coordinators to support transparency and decision-making.
   ```

   ![Enter agent description](assets/102_paste_description.png)

7. Click "Create" to initialize your agent

   ![Click Create button](assets/103_create.png)

### 2. Importing and Attaching Tools

1. Click "Add tool"

   ![Click Add tool](assets/104_add_tool.png)

2. Select "Import an external tool."

   ![Select Import](assets/105_import.png)

3. Click on the upload area labeled "Drag and drop OpenAPI files here or click to upload."

   ![Click upload area](assets/106_upload.png)

4. Upload the file containing the OpenAPI specification file: `openapi-tools-report.json`

5. Click "Next"

   ![Click Next](assets/107_next.png)

6. Click "Select all rows in the table" to select all available tools

   ![Select all rows](assets/108_select_all_rows.png)

7. Click "Done"

   ![Click Done](assets/109_done.png)

2. Click "Deploy" to activate your AskReporting agent

   ![Test Agent](assets/110_deploy.png)

### 3. Switching to and Testing the Agent

1. Click on the menu icon in the top left corner

   ![Navigate to Menu](assets/111_hamburger.png)

2. Click on "Chat" 

   ![Navigate to Chat](assets/112_chat.png)

3. Click "AskBenefits" Dropdown

   ![Chat Selection](assets/113_chat_selection.png)

4. Select "AskReporting" 

   ![Navigate to Chat](assets/114_askreporting.png)

---

## Final Testing Scenarios

After successful deployment, test the AskReporting agent with the following sample prompts to verify functionality, clicking the generated urls to view reports:

1. **Ask for a Default Report:**
   ```
   Please create a care report
   ```

2. **Ask for a Custom Report:**
   ```
   Please create a care report with an additional section that translates the email from the provider into layman terms 
   ```
