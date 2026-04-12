// https://docs.astro.build/en/reference/modules/astro-content/#definecollection

import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const trades = defineCollection({
  loader: glob({ pattern: ['*.md', '*.mdx'], base: 'src/trades' }),
  schema: z.object({
    title: z.string(),
    ticker: z.string(),
    entryDate: z.date(),
    entryTime: z.string(),
    exitDate: z.date().optional(),
    exitTime: z.string(),
    strategy: z.string(),
    direction: z.string(),
    risk: z.number(),
    pl: z.number()
  }),
});

export const collections = { trades };