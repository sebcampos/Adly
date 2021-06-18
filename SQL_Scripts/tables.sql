-- Table: public.customer

-- DROP TABLE public.customer;

CREATE TABLE IF NOT EXISTS public.customer
(
    userid integer NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    lastname character varying(255) COLLATE pg_catalog."default" NOT NULL,
    firstname character varying(255) COLLATE pg_catalog."default" NOT NULL,
    age integer,
    birthdate date,
    gender character varying(255) COLLATE pg_catalog."default",
    phone integer,
    CONSTRAINT customer_pkey PRIMARY KEY (userid)
)

TABLESPACE pg_default;

ALTER TABLE public.customer
    OWNER to postgres;


-- Table: public.interest

-- DROP TABLE public.interest;

CREATE TABLE IF NOT EXISTS public.interest
(
    "interestID" integer NOT NULL,
    category1 character varying(255) COLLATE pg_catalog."default" NOT NULL,
    category2 character varying(255) COLLATE pg_catalog."default",
    category3 character varying(255) COLLATE pg_catalog."default",
    category4 character varying(255) COLLATE pg_catalog."default",
    category5 character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT interest_pkey PRIMARY KEY ("interestID")
)

TABLESPACE pg_default;

ALTER TABLE public.interest
    OWNER to postgres;
