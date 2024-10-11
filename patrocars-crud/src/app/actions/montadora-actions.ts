"use server";

import { db } from "../_lib/prisma";
import { Montadora, Prisma } from "@prisma/client";
import { revalidatePath } from "next/cache";

export type MontadoraData = {
  id: string;
  nome: string;
  pais: string;
  anoFundacao: number;
};

type Result = {
  success: boolean;
  message: string;
};

export async function getMontadoraById(id: string) {
  const montadora = await db.montadora.findUnique({
    where: { id },
  });

  if (!montadora) {
    throw new Error("Montadora não encontrado");
  }

  return montadora;
}


export async function getMontadoras() {
  return db.montadora.findMany();
}

export async function removeMontadora(id: string): Promise<Result> {
  const result: Result = { success: false, message: "" };

  try {
    await db.montadora.delete({ where: { id } });

    result.success = true;
    result.message = "Montadora removido com sucesso!";

    revalidatePath(`/montadora/${id}`);
  } catch (error) {
    result.message = `Erro ao remover montadora: ${error}`;
  }

  return result;
}

export async function upsertMontadora({
	id,
	nome,
	pais,
	anoFundacao,
}: MontadoraData) {
	const result: Result = { success: false, message: "" };

	try {
		const newMontadora = await db.montadora.upsert({
			where: { id: id ?? "" },
			update: {
				nome,
				pais,
				anoFundacao,
			},
			create: {
				nome,
				pais,
				anoFundacao,
			},
		});

		result.success = true;
		result.message = `Montadora ${newMontadora.nome} criado com sucesso!`;

		revalidatePath("/montadoras");
	} catch (error) {
		if (error instanceof Prisma.PrismaClientKnownRequestError) {
			if (error.code === "P2002") {
				result.message = `Montadora ${name} ja existe`;
			} else {
				result.message = `Erro ao criar montadora: ${error.message}`;
			}
		}

		console.error(error);
	}

	return result;
}


