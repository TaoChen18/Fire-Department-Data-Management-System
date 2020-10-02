CREATE TABLE IF NOT EXISTS  incident
(
    incident_id numeric,
    datetime date,
    alarm_box_borough text,
    alarm_box_number numeric,
    alarm_box_location text,
    incident_borough text,
    zipcode text,
    policeprecinct numeric,
    citycouncildistrict numeric,
    communitydistrict numeric,
    communityschooldistrict numeric,
    congressionaldistrict numeric,
    alarm_source text,
    alarm_level text,
    highest_level text,
    classification text,
    classification_group text,
    dispatch_response_second numeric,
    first_assign date,
    first_activate date,
    first_on_scene date,
    incident_close date,
    valid_dispatch_rspns_time text,
    valid_incident_rspns_time text,
    incident_response_second numeric,
    incident_travel_second numeric,
    engines_assigned numeric,
    ladders_assigned numeric,
    other_assigned numeric
);