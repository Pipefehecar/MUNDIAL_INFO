--equipos
INSERT INTO public.equipo (id, nombre, bandera_img, escudo_img, created_at) VALUES (1, 'ARGENTINA', NULL, NULL, '2022-07-01 11:39:44.685207-05');
INSERT INTO public.equipo (id, nombre, bandera_img, escudo_img, created_at) VALUES (2, 'ALEMANIA', NULL, NULL, '2022-07-01 13:34:07.077482-05');
INSERT INTO public.equipo (id, nombre, bandera_img, escudo_img, created_at) VALUES (3, 'COLOMBIA', NULL, NULL, '2022-07-01 13:34:19.969709-05');
INSERT INTO public.equipo (id, nombre, bandera_img, escudo_img, created_at) VALUES (4, 'BRAZIL', NULL, NULL, '2022-07-01 13:34:52.159421-05');
INSERT INTO public.equipo (id, nombre, bandera_img, escudo_img, created_at) VALUES (5, 'SUIZA', 'band', NULL, '2022-07-01 11:33:00.023487-05');

--jugadores
INSERT INTO public.jugador (id, foto, nombre, apellido, fecha_nacimiento, numero_camiseta, es_titular, posicion, created_at, equipo_id_id) VALUES (1, NULL, 'Julio', 'barreneche', '1998-03-21', 25, false, 'MI', '2022-07-01 14:49:45.013419-05', 5);
INSERT INTO public.jugador (id, foto, nombre, apellido, fecha_nacimiento, numero_camiseta, es_titular, posicion, created_at, equipo_id_id) VALUES (2, NULL, 'Nicolas', 'Panamera', '1997-05-22', 25, false, 'MI', '2022-07-01 14:50:57.808256-05', 4);


--directivos
INSERT INTO public.directivo (id, nombre, apellido, fecha_nacimiento, nacionalidad, rol, created_at, equipo_id_id) VALUES (1, 'Julio', 'barreneche', '1955-02-25', 'Colombiano', 'TEC', '2022-07-01 14:46:29.87802-05', 3);
INSERT INTO public.directivo (id, nombre, apellido, fecha_nacimiento, nacionalidad, rol, created_at, equipo_id_id) VALUES (2, 'Juan Carlos', 'Martinez', '1965-07-29', 'Colombiano', 'MED', '2022-07-01 14:47:27.202454-05', 4);
INSERT INTO public.directivo (id, nombre, apellido, fecha_nacimiento, nacionalidad, rol, created_at, equipo_id_id) VALUES (3, 'Carlos', 'Sosa', '1976-08-19', 'Panameño', 'PRE', '2022-07-01 14:48:09.721876-05', 5);