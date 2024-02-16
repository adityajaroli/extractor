Feature: Testing behavior of Extraction service
  As a service owner, I would like to test the endpoints of Extraction service

Scenario: service health
  When user makes get request to /health endpoint
  Then the request should be completed with status code 200

Scenario: extraction
  When user starts extraction process for the date 2021-01-01
  Then the request should be completed with status code 200
  And the response should have following properties: extract_date,total_records,status
  And in the response, extract_date should be 2021-01-01
  And in the response, total_records should be 1000
  And in the response, status should be successful
  And the data should be available in the DB for the date 2021-01-01 and count should be 1000