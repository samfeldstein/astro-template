// https://docs.astro.build/en/reference/modules/astro-content/#definecollection

import { defineCollection, reference } from 'astro:content';
import { z } from 'astro/zod';
import { file } from 'astro/loaders';
// import { glob } from 'astro/loaders';

const tradesData = defineCollection({
  loader: file("src/data/trades.yml"),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    ticker: z.string(),
    entryDate: z.coerce.date(),
    entryTime: z.string(),
    exitDate: z.coerce.date().optional(),
    exitTime: z.string(),
    strategy: z.string(),
    direction: z.string(),
    risk: z.number(),
    pl: z.number(),
    notes: z.string(),
  }),
});

// const tradeNotes = defineCollection({
//   loader: glob({ pattern: ['*.md', '*.mdx'], base: 'src/trades' }),
//   schema: z.object({
//     id: reference('tradesData'),
//   }),
// });

export const collections = { tradesData };