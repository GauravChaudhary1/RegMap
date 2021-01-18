# Regulation Requirement Mapping to Controls

## GRC Focus Area - Auditors' Perspective

Every industry is administered by one or multiple regulations. For instance, just in the US, there are at least ten different financial regulators with hundreds of regulation requirements that apply to different entities to ensure the integrity and cohesion of the economic system as well as to conserve the interests of common people.
This does not only complicate the enforcement process for the regulators but also makes things hard to track for the entities that need to comply with these regulations.
Regulatory management is still one of the most manual GRC tasks. Authorities provide a detailed document to the users who are then responsible for reading, understanding, creating Regulation Requirements and then mapping it to the entities manually. This is a cumbersome task and takes a lot of manual efforts.
Further, Auditors usually pull deficient controls and sample of passed controls to review them and ensure the control was applied as designed. This again is a manual process and equally tiresome.

<br>
<Br>

The idea is, to make regulatory compliance smart to reduce the manual efforts invested in reading the document and then creating/reviewing the requirements in the GRC system.
This can be achieved by making the systems intelligent, so that, once we provide a document, it should be able to process the provided document’s content and infer the Requirements of regulations. Further, the system should also be able to create these requirements in the system and suggest the appropriate mapping with controls. 

<br>

## High Level Diagram - Technical Architecture

![](/Images/HLD.png)


## Execution of Idea - 3 Phases

Phase 1:
1. Creation of Similarity matrix and mapping existing controls to the query made by Auditor.
2. Design an API using python and deploy to the SAP API Hub for active instance of API.

<br>
Phase 2:
1. Take the input in three major forms. Free text, Excel Document of Requirement, Audit Document.
2. If input is Audit document, use NLP Summarize to summarize the Data.
3. Feed the information to matrix created.
<br>
Phase 3:
1. Designing of UI using Angular 9.