CREATE TABLE IF NOT EXISTS services (
    ts timestamp NOT NULL,
    name text,
    category text,
    price INTEGER,
    location GEOMETRY(Point, 4326) NOT NULL
);

CREATE INDEX i_coors_goods_location ON services USING GIST (location);
