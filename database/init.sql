-- history of all coordinates from all users
CREATE TABLE IF NOT EXISTS coordinates_history (
    id bigserial PRIMARY KEY,
    installation_id VARCHAR (128) NOT NULL,
    ts timestamp NOT NULL,
    location GEOMETRY(Point, 4326) NOT NULL
);
CREATE INDEX i_coors_history_location ON coordinates_history USING GIST (location);

-- current location of user
CREATE TABLE IF NOT EXISTS user_coordinates (
    id bigserial PRIMARY KEY,
    installation_id VARCHAR (128) NOT NULL,
    location GEOMETRY(Point, 4326) NOT NULL,
    updated_ts timestamp NOT NULL
);
CREATE UNIQUE INDEX i_user_coors_installation_id ON user_coordinates (installation_id);
CREATE INDEX i_user_coors_location ON user_coordinates USING GIST (location);

-- threat area
CREATE TABLE IF NOT EXISTS threat_areas (
    id bigserial PRIMARY KEY,
    description text,
    location GEOMETRY(Point, 4326) NOT NULL,
    ts timestamp NOT NULL,
    is_new BOOLEAN DEFAULT TRUE,
    active boolean,
    threat_type TEXT
);
CREATE INDEX i_threat_areas_location ON threat_areas USING GIST (location);

CREATE TABLE IF NOT EXISTS users (
    id bigserial PRIMARY KEY,
    installation_id VARCHAR (128) NOT NULL,
    device_id VARCHAR (128) NOT NULL,
    notify_me BOOLEAN DEFAULT TRUE,
    active BOOLEAN,
    created_ts timestamp NOT NULL,
    updated_ts timestamp NOT NULL,
    disabled_ts timestamp NULL
);
CREATE UNIQUE INDEX i_devices_installation_id ON users (installation_id);
