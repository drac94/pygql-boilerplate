-- Table Definition ----------------------------------------------

CREATE TABLE post (
    id uuid PRIMARY KEY,
    title text NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, CURRENT_TIMESTAMP),
    updated_at timestamp without time zone NOT NULL DEFAULT timezone('utc'::text, CURRENT_TIMESTAMP)
);