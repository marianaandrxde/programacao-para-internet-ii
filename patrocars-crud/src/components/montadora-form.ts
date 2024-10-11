"use client";

import { upsertMontadora } from "@/app/actions/montadora-actions";
import {zodResolver} from "@hookform/resolvers/zod";
import {useForm} from "react-hook-form";
import {z} from "zod";
import {useRouter} from "next/navigation";
import {toast} from "./ui/use-toast"

type MontadoraProps = {
    montadora?: {
        id?: string;
        nome: string;
        pais: string;
        anoFundacao: number;  
    };
};

const formSchema = z.object({
    nome: z
        .string()
        .min(2, {message: "O nome deve conter pelo menos 2 caracteres"}),
    pais: z
        .string(),
    anoFundacao: z
        .number(),
});

export function MontadoraForm({montadora}: MontadoraProps) {
    const router = useRouter();

    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            nome: montadora?.nome ?? "",
            pais: montadora?.pais ?? "",
            anoFundacao: montadora?.anoFundacao ?? undefined,
        },
    });

    async function onSubmit(values: z.infer<typeof formSchema>) {
        const result = await upsertMontadora({
            id: montadora?.id ?? "",
            nome: values.nome?? "",
            pais: values.pais,
            anoFundacao: values.anoFundacao as number,
        });

        toast({
            title: result.success
                ? "Alterações salvas com sucesso!"
                : "Erro ao salvar...",
            variant: result.success ? undefined : "destructive",
            description: result.message,
            duration: 3000,
        });

        if(result.success) {
            router.push(`/montadoras/${montadora?.id}/`);
        }
    }
   
    // return (

    // );
}
