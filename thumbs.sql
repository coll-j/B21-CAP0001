--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    question_id integer NOT NULL,
    mapping_level_id integer NOT NULL,
    text character varying NOT NULL
);


ALTER TABLE public.answer OWNER TO kuuhaku86;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO kuuhaku86;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: badge; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.badge (
    id integer NOT NULL,
    title character varying NOT NULL,
    description text NOT NULL,
    gambar text NOT NULL
);


ALTER TABLE public.badge OWNER TO kuuhaku86;

--
-- Name: badge_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.badge_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.badge_id_seq OWNER TO kuuhaku86;

--
-- Name: badge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.badge_id_seq OWNED BY public.badge.id;


--
-- Name: blacklist_tokens; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.blacklist_tokens (
    id integer NOT NULL,
    token character varying NOT NULL,
    blacklisted_on timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.blacklist_tokens OWNER TO kuuhaku86;

--
-- Name: blacklist_tokens_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.blacklist_tokens_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blacklist_tokens_id_seq OWNER TO kuuhaku86;

--
-- Name: blacklist_tokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.blacklist_tokens_id_seq OWNED BY public.blacklist_tokens.id;


--
-- Name: facts; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.facts (
    id integer NOT NULL,
    question_id integer NOT NULL,
    text character varying NOT NULL
);


ALTER TABLE public.facts OWNER TO kuuhaku86;

--
-- Name: facts_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.facts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facts_id_seq OWNER TO kuuhaku86;

--
-- Name: facts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.facts_id_seq OWNED BY public.facts.id;


--
-- Name: feedback; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.feedback (
    id integer NOT NULL,
    level_id integer NOT NULL,
    response integer NOT NULL,
    text_feedback text NOT NULL,
    answer_id integer NOT NULL,
    answer_result boolean
);


ALTER TABLE public.feedback OWNER TO kuuhaku86;

--
-- Name: feedback_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.feedback_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feedback_id_seq OWNER TO kuuhaku86;

--
-- Name: feedback_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.feedback_id_seq OWNED BY public.feedback.id;


--
-- Name: level; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.level (
    id integer NOT NULL,
    level integer NOT NULL,
    branch integer NOT NULL,
    public_link text NOT NULL
);


ALTER TABLE public.level OWNER TO kuuhaku86;

--
-- Name: level_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.level_id_seq OWNER TO kuuhaku86;

--
-- Name: level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.level_id_seq OWNED BY public.level.id;


--
-- Name: mapping_level; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.mapping_level (
    id integer NOT NULL,
    level_before integer NOT NULL,
    level_next integer NOT NULL,
    answer_result boolean
);


ALTER TABLE public.mapping_level OWNER TO kuuhaku86;

--
-- Name: mapping_level_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.mapping_level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mapping_level_id_seq OWNER TO kuuhaku86;

--
-- Name: mapping_level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.mapping_level_id_seq OWNED BY public.mapping_level.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.question (
    id integer NOT NULL,
    level_id integer NOT NULL,
    text character varying NOT NULL,
    is_multiple_choices boolean DEFAULT true NOT NULL
);


ALTER TABLE public.question OWNER TO kuuhaku86;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO kuuhaku86;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying NOT NULL,
    username character varying NOT NULL,
    password text NOT NULL
);


ALTER TABLE public."user" OWNER TO kuuhaku86;

--
-- Name: user_badge; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.user_badge (
    id integer NOT NULL,
    user_id integer NOT NULL,
    badge_id integer NOT NULL
);


ALTER TABLE public.user_badge OWNER TO kuuhaku86;

--
-- Name: user_badge_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.user_badge_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_badge_id_seq OWNER TO kuuhaku86;

--
-- Name: user_badge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.user_badge_id_seq OWNED BY public.user_badge.id;


--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO kuuhaku86;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: user_levels; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.user_levels (
    id integer NOT NULL,
    user_id integer NOT NULL,
    level_id integer NOT NULL
);


ALTER TABLE public.user_levels OWNER TO kuuhaku86;

--
-- Name: user_levels_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.user_levels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_levels_id_seq OWNER TO kuuhaku86;

--
-- Name: user_levels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.user_levels_id_seq OWNED BY public.user_levels.id;


--
-- Name: user_response; Type: TABLE; Schema: public; Owner: kuuhaku86
--

CREATE TABLE public.user_response (
    id integer NOT NULL,
    level_id integer NOT NULL,
    user_id integer NOT NULL,
    response_text text,
    response_option bigint[],
    response_prediction_result bigint[] NOT NULL,
    response_answer_id integer
);


ALTER TABLE public.user_response OWNER TO kuuhaku86;

--
-- Name: user_response_id_seq; Type: SEQUENCE; Schema: public; Owner: kuuhaku86
--

CREATE SEQUENCE public.user_response_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_response_id_seq OWNER TO kuuhaku86;

--
-- Name: user_response_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kuuhaku86
--

ALTER SEQUENCE public.user_response_id_seq OWNED BY public.user_response.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: badge id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.badge ALTER COLUMN id SET DEFAULT nextval('public.badge_id_seq'::regclass);


--
-- Name: blacklist_tokens id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.blacklist_tokens ALTER COLUMN id SET DEFAULT nextval('public.blacklist_tokens_id_seq'::regclass);


--
-- Name: facts id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.facts ALTER COLUMN id SET DEFAULT nextval('public.facts_id_seq'::regclass);


--
-- Name: feedback id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.feedback ALTER COLUMN id SET DEFAULT nextval('public.feedback_id_seq'::regclass);


--
-- Name: level id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.level ALTER COLUMN id SET DEFAULT nextval('public.level_id_seq'::regclass);


--
-- Name: mapping_level id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.mapping_level ALTER COLUMN id SET DEFAULT nextval('public.mapping_level_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: user_badge id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_badge ALTER COLUMN id SET DEFAULT nextval('public.user_badge_id_seq'::regclass);


--
-- Name: user_levels id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_levels ALTER COLUMN id SET DEFAULT nextval('public.user_levels_id_seq'::regclass);


--
-- Name: user_response id; Type: DEFAULT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_response ALTER COLUMN id SET DEFAULT nextval('public.user_response_id_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.answer (id, question_id, mapping_level_id, text) FROM stdin;
\.


--
-- Data for Name: badge; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.badge (id, title, description, gambar) FROM stdin;
1	level 1	great	great
2	level 2	great too	great too
\.


--
-- Data for Name: blacklist_tokens; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.blacklist_tokens (id, token, blacklisted_on) FROM stdin;
1	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjI1NjY2MTIsImlhdCI6MTYyMjQ4MDIwNywic3ViIjoxfQ.Et_rQeLqW2WRDYu8t2YJSV-rLR2-1mLTRY7wIqxbtGE	2021-06-01 00:03:32
\.


--
-- Data for Name: facts; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.facts (id, question_id, text) FROM stdin;
\.


--
-- Data for Name: feedback; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.feedback (id, level_id, response, text_feedback, answer_id, answer_result) FROM stdin;
\.


--
-- Data for Name: level; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.level (id, level, branch, public_link) FROM stdin;
1	1	1	http://127.0.0.1:5000
2	2	1	http://127.0.0.1:5000
\.


--
-- Data for Name: mapping_level; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.mapping_level (id, level_before, level_next, answer_result) FROM stdin;
1	1	2	\N
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.question (id, level_id, text, is_multiple_choices) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public."user" (id, email, username, password) FROM stdin;
1	king@email.com	kuuhaku86	$2b$13$iPbsU3K8in9n/8lYas1pO.DuOZnyl6X.dJvSAprrFSilvJfzjwQLe
\.


--
-- Data for Name: user_badge; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.user_badge (id, user_id, badge_id) FROM stdin;
2	1	2
\.


--
-- Data for Name: user_levels; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.user_levels (id, user_id, level_id) FROM stdin;
\.


--
-- Data for Name: user_response; Type: TABLE DATA; Schema: public; Owner: kuuhaku86
--

COPY public.user_response (id, level_id, user_id, response_text, response_option, response_prediction_result, response_answer_id) FROM stdin;
\.


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.answer_id_seq', 1, false);


--
-- Name: badge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.badge_id_seq', 2, true);


--
-- Name: blacklist_tokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.blacklist_tokens_id_seq', 1, true);


--
-- Name: facts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.facts_id_seq', 1, false);


--
-- Name: feedback_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.feedback_id_seq', 1, false);


--
-- Name: level_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.level_id_seq', 2, true);


--
-- Name: mapping_level_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.mapping_level_id_seq', 1, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.question_id_seq', 1, false);


--
-- Name: user_badge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.user_badge_id_seq', 2, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- Name: user_levels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.user_levels_id_seq', 1, false);


--
-- Name: user_response_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kuuhaku86
--

SELECT pg_catalog.setval('public.user_response_id_seq', 1, false);


--
-- Name: answer answer_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_pk PRIMARY KEY (id);


--
-- Name: badge badge_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.badge
    ADD CONSTRAINT badge_pk PRIMARY KEY (id);


--
-- Name: blacklist_tokens blacklist_tokens_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.blacklist_tokens
    ADD CONSTRAINT blacklist_tokens_pk PRIMARY KEY (id);


--
-- Name: facts facts_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.facts
    ADD CONSTRAINT facts_pk PRIMARY KEY (id);


--
-- Name: feedback feedback_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_pk PRIMARY KEY (id);


--
-- Name: level level_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.level
    ADD CONSTRAINT level_pk PRIMARY KEY (id);


--
-- Name: mapping_level mapping_level_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.mapping_level
    ADD CONSTRAINT mapping_level_pk PRIMARY KEY (id);


--
-- Name: question question_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pk PRIMARY KEY (id);


--
-- Name: user_badge user_badge_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_badge
    ADD CONSTRAINT user_badge_pk PRIMARY KEY (id);


--
-- Name: user_levels user_levels_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_levels
    ADD CONSTRAINT user_levels_pk PRIMARY KEY (id);


--
-- Name: user user_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pk PRIMARY KEY (id);


--
-- Name: user_response user_response_pk; Type: CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_response
    ADD CONSTRAINT user_response_pk PRIMARY KEY (id);


--
-- Name: answer answer_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_fk FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: answer answer_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_fk_1 FOREIGN KEY (mapping_level_id) REFERENCES public.mapping_level(id);


--
-- Name: facts facts_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.facts
    ADD CONSTRAINT facts_fk FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: feedback feedback_answer_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_answer_fk FOREIGN KEY (answer_id) REFERENCES public.answer(id);


--
-- Name: feedback feedback_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_fk FOREIGN KEY (level_id) REFERENCES public.level(id);


--
-- Name: mapping_level mapping_level_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.mapping_level
    ADD CONSTRAINT mapping_level_fk FOREIGN KEY (level_before) REFERENCES public.level(id);


--
-- Name: mapping_level mapping_level_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.mapping_level
    ADD CONSTRAINT mapping_level_fk_1 FOREIGN KEY (level_next) REFERENCES public.level(id);


--
-- Name: question question_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_fk FOREIGN KEY (level_id) REFERENCES public.level(id);


--
-- Name: user_badge user_badge_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_badge
    ADD CONSTRAINT user_badge_fk FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: user_badge user_badge_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_badge
    ADD CONSTRAINT user_badge_fk_1 FOREIGN KEY (badge_id) REFERENCES public.badge(id);


--
-- Name: user_levels user_levels_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_levels
    ADD CONSTRAINT user_levels_fk FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: user_levels user_levels_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_levels
    ADD CONSTRAINT user_levels_fk_1 FOREIGN KEY (level_id) REFERENCES public.level(id);


--
-- Name: user_response user_response_answer_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_response
    ADD CONSTRAINT user_response_answer_fk FOREIGN KEY (response_answer_id) REFERENCES public.answer(id);


--
-- Name: user_response user_response_fk; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_response
    ADD CONSTRAINT user_response_fk FOREIGN KEY (level_id) REFERENCES public.level(id);


--
-- Name: user_response user_response_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: kuuhaku86
--

ALTER TABLE ONLY public.user_response
    ADD CONSTRAINT user_response_fk_1 FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

